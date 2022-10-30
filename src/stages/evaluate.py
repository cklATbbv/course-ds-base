import yaml
import pandas as pd
import joblib
from sklearn.metrics import confusion_matrix, f1_score
#from src.report.plot_confusion_matrix import plot_confusion_matrix

import numpy as np
import matplotlib.pyplot as plt
import itertools


def plot_confusion_matrix(cm,
                          target_names,
                          title='Confusion matrix',
                          cmap=None,
                          normalize=True):
    """
    given a sklearn confusion matrix (cm), make a nice plot

    Arguments
    ---------
    cm:           confusion matrix from sklearn.metrics.confusion_matrix

    target_names: given classification classes such as [0, 1, 2]
                  the class names, for example: ['high', 'medium', 'low']

    title:        the text to display at the top of the matrix

    cmap:         the gradient of the values displayed from matplotlib.pyplot.cm
                  see http://matplotlib.org/examples/color/colormaps_reference.html
                  plt.get_cmap('jet') or plt.cm.Blues

    normalize:    If False, plot the raw numbers
                  If True, plot the proportions

    Usage
    -----
    plot_confusion_matrix(cm           = cm,                  # confusion matrix created by
                                                              # sklearn.metrics.confusion_matrix
                          normalize    = True,                # show proportions
                          target_names = y_labels_vals,       # list of names of the classes
                          title        = best_estimator_name) # title of graph

    Citiation
    ---------
    http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html

    """

    accuracy = np.trace(cm) / float(np.sum(cm))
    misclass = 1 - accuracy

    if cmap is None:
        cmap = plt.get_cmap('Blues')

    fig, ax = plt.subplots(figsize=(8, 6))
    t = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.set_title(title)
    fig.colorbar(t)

    if target_names is not None:
        tick_marks = np.arange(len(target_names))
        ax.set_xticks(tick_marks, target_names, rotation=45)
        ax.set_yticks(tick_marks, target_names)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    thresh = cm.max() / 1.5 if normalize else cm.max() / 2
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        if normalize:
            ax.text(j, i, "{:0.4f}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")
        else:
            ax.text(j, i, "{:,}".format(cm[i, j]),
                     horizontalalignment="center",
                     color="white" if cm[i, j] > thresh else "black")

    fig.tight_layout()
    ax.set_ylabel('True label')
    ax.set_xlabel('Predicted label\naccuracy={:0.4f}; misclass={:0.4f}'.format(accuracy, misclass))
    
    return fig, ax 

def evaluate(config_path):

    with open(config_path) as fid:
        config = yaml.safe_load(fid)

    
    test_dataset = pd.read_csv(config['evaluate']["input_file"])

    y_test = test_dataset.loc[:, 'target'].values.astype('int32')
    X_test = test_dataset.drop('target', axis=1).values.astype('float32')


    model = joblib.load(config['evaluate']['model_file'])

    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_pred, y_test)
    f1 = f1_score(y_true = y_test, y_pred = y_pred, average='macro')


    fig, ax = plot_confusion_matrix(cm, ['a','b','c'], normalize=False)
    fig.savefig(config['evaluate']['confusion_matrix_png'], transparent=True)


if __name__ == '__main__':
    
    import argparse
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--config', dest='config', required=True)
    args = arg_parser.parse_args()

    evaluate(config_path=args.config)

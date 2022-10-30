import yaml
import pandas as pd
import joblib
from sklearn.metrics import confusion_matrix, f1_score
from src.report.plot_confusion_matrix import plot_confusion_matrix

def evaluate(config_path):

    with open(config_path) as fid:
        config = yaml.safe_load(fid)

    
    test_dataset = pd.read_csv(config["input_file"])

    y_test = test_dataset.loc[:, 'target'].values.astype('int32')
    X_test = test_dataset.drop('target', axis=1).values.astype('float32')


    model = joblib.load(config['model_file'])

    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_pred, y_test)
    f1 = f1_score(y_true = y_test, y_pred = y_pred, average='macro')


    fig, ax = plot_confusion_matrix(cm, ['a','b','c'], normalize=False)
    fig.savefig(config['confusion_matrix_png'], transparent=True)


if __name__ == '__main__':
    
    import argparse
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--config', dest='config', required=True)
    args = arg_parser.parse_args()

    evaluate(config_path=args.config)

import yaml
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression

def train(config_path):

    with open(config_path) as fid:
        config = yaml.safe_load(fid)

    
    train_dataset = pd.read_csv(config['train']["input_file"])

    y_train = train_dataset.loc[:, 'target'].values.astype('int32')
    X_train = train_dataset.drop('target', axis=1).values.astype('float32')

    logreg = LogisticRegression(**config['train']['model_param'])
    logreg.fit(X_train, y_train)

    joblib.dump(logreg, config['train']['model_file'])




if __name__ == '__main__':
    
    import argparse
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--config', dest='config', required=True)
    args = arg_parser.parse_args()

    train(config_path=args.config)

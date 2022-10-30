import yaml
import pandas as pd

from sklearn.model_selection import train_test_split


def data_split(config_path):

    with open(config_path) as fid:
        config = yaml.safe_load(fid)

    test_size=config['test_size']
    random_state=config['random_state']
    
    dataset = pd.read_csv(config['input_file'])
    train_dataset, test_dataset = train_test_split(dataset, 
                                                   test_size=test_size,
                                                   random_state=random_state)

    train_dataset.to_csv(config["output_file_train_data"], index=False)
    test_dataset.to_csv(config["output_file_test_data"], index=False)


if __name__ == '__main__':
    
    import argparse
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--config', dest='config', required=True)
    args = arg_parser.parse_args()

    data_split(config_path=args.config)
import pandas as pd
from typing import Text
import yaml

def featurize(config_path: Text) -> None:

    with open(config_path) as fid:
        config = yaml.safe_load(fid)

    dataset = pd.read_csv(config['input_file'])
    dataset['sepal_length_to_sepal_width'] = dataset['sepal_length'] / dataset['sepal_width']
    dataset['petal_length_to_petal_width'] = dataset['petal_length'] / dataset['petal_width']

    dataset.to_csv(config["output_file"], index=False)

if __name__ == '__main__':
    
    import argparse
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--config', dest='config', required=True)
    args = arg_parser.parse_args()

    featurize(config_path=args.config)
    
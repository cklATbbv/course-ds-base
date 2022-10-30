
import yaml
import pandas as pd
from sklearn.datasets import load_iris
from typing import Text

def data_download(config_path: Text):

    with open(config_path) as fid:
        config = yaml.safe_load(fid)
        
    # Get data     
    data = load_iris(as_frame=True)
    dataset = data.frame
    
    # feature names
    dataset.columns = [colname.strip(' (cm)').replace(' ', '_') for colname in dataset.columns.tolist()]
    dataset.to_csv(config['output_file'])
    
    print("Data download is complete.")
    
    
    
if __name__ == '__main__':
    
    import argparse
    
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--config', dest='config', required=True)
    
    args = arg_parser.parse_args()
    
    data_download(config_path=args.config)
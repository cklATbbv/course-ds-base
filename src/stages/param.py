import yaml
import os.path as path

#Note there are different sorts of parameters for stages
# 
# - stage internal
# - stage interface
# 
# The following "yaml"  dictionary is structured accordingly

homefolder = "/home/cedric/Courses/course-ds-base"

parameters = {

    "download" : {

    },

    "download2featurize": {
        "raw_data_path" : path.join(homefolder, 'data', 'raw', 'iris.csv')
    },
    
    "featurize": {
        
    },

    "featurize2split": {
        "featurized_data_path": path.join(homefolder, "data", "featurized", "iris_features.csv")
    },

    "split" : {
        "test_size": 0.2,
        "random_state": 42
    },

    
    "split2train" :{
        "train_data_path": path.join(homefolder, "data", "split", "train.csv"),
    },

    "split2evaluate" :{
        "test_data_path": path.join(homefolder, "data", "split", "test.csv")
    },

    "train": {

        "model_name": "logreg",

        "model_params": {
            "C": 0.001,
            "solver": 'lbfgs',
            "multi_class": 'multinomial',
            "max_iter": 100
        },
    },

    "train2evaluate": {
        "model_path": path.join(homefolder, "models", "model.joblib")
    }, 

    "evaluate": {
        "confusion_matrix_png": path.join(homefolder, "reports", "confusion_matrix.png")
    }

}

download_params = {
    "output_file": parameters["download2featurize"]['raw_data_path']
}

yaml.dump(download_params, open(path.join(homefolder,"config", "param_download.yml"),"w"))


featurize_params = {
    "input_file": parameters["download2featurize"]['raw_data_path'],
    "output_file": parameters["featurize2split"]['featurized_data_path']
}

yaml.dump(featurize_params, open(path.join(homefolder,"config", "param_featurize.yml"),"w"))
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

split_params = {
    "test_size": parameters["split"]["test_size"],
    "random_state": parameters["split"]["random_state"],
    "input_file": parameters["featurize2split"]["featurized_data_path"],
    "output_file_train_data": parameters["split2train"]["train_data_path"],
    "output_file_test_data": parameters["split2evaluate"]["test_data_path"]
}

yaml.dump(split_params, open(path.join(homefolder,"config", "param_split.yml"),"w"))


train_params = {
    "model_name": parameters["train"]["model_name"],
    "model_param": parameters["train"]["model_params"],
    "input_file": parameters["split2train"]["train_data_path"],
    "model_file": parameters["train2evaluate"]["model_path"]
}

yaml.dump(train_params, open(path.join(homefolder,"config", "param_train.yml"),"w"))

evaluate_params = {
    "input_file": parameters["split2evaluate"]["test_data_path"],
    "model_file": parameters["train2evaluate"]["model_path"],
    "confusion_matrix_png": parameters["evaluate"]["confusion_matrix_png"]
}

yaml.dump(evaluate_params, open(path.join(homefolder,"config", "param_evaluate.yml"),"w"))



parameter_file = {

    "download": download_params,
    "featurize": featurize_params,
    "split": split_params,
    "train": train_params,
    "evaluate": evaluate_params

}

yaml.dump(parameter_file, open(path.join(homefolder,"params.yaml"),"w"))

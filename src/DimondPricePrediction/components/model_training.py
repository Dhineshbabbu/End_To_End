import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from src.DimondPricePrediction.exeception import customException
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.utils.utils import save_object,evaluate_model
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

@dataclass
class ModelTrainingConfig:
    training_model_file_path=os.path.join('artifacts','model.pkl')


class ModelTraining:
    def __init__(self):
        self.model_training_config=ModelTrainingConfig()

    def initiat_model_training(self,train_array,test_array):
        try:
            logging.info('Spliting Dependent and Independent variable from train and test data')
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={
                'LinerRegression': LinearRegression(),
                'Ridge':Ridge(),
                'Lasso':Lasso(),
                'Elastic Net':ElasticNet()
            }

            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            logging.info(f"Model Report:{model_report.values()}")

            best_model_score=max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model=models[best_model_name]

            logging.info(f"Best Model Found, Model Name :{best_model_name},R2 Score :{best_model_score}")

            save_object(
                file_path=self.model_training_config.training_model_file_path,
                obj=best_model
            )

        except Exception as e:
            logging.info("Exception occured at model Training")
            raise customException(e,sys)


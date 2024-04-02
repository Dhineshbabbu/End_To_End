import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass
from src.DimondPricePrediction.exeception import customException
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.utils.utils import save_object
from sklearn.impute import SimpleImputer # --> To Handling Missing values
from sklearn.preprocessing import StandardScaler # --> To Handling Feature Scaling
from sklearn.preprocessing import OrdinalEncoder # --> To Perform Encoding
# ---- To Perform Pipeline ------
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer # --> New to meeee


class DataTransformationConfig:
    perprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformation(self):
        try:
            logging.info('Data Transformation started')
            #numerical and categorical varialbe
            num_col=['carat', 'depth', 'table', 'x', 'y', 'z']
            cat_col=['cut', 'color', 'clarity']

            #categories
            cut_cat=['Premium', 'Very Good', 'Ideal', 'Good', 'Fair']
            color_cat=['F', 'J', 'G', 'E', 'D', 'H', 'I']
            clarity_cat=['VS2', 'SI2', 'VS1', 'SI1', 'IF', 'VVS2', 'VVS1', 'I1']

            logging.info('Pipeline Initiated')

            # Numerical Pipeline
            num_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer()),
                    ('scaler',StandardScaler())
                ]
            )

            #Categorical Pipeline
            cat_pipeline=Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequent')),
                    ('ordinalencode',OrdinalEncoder(categories=[cut_cat,color_cat,clarity_cat]))
                ]
            )

            #Column Transformation
            preprocessor=ColumnTransformer(
                [
                    ('num_pipeline',num_pipeline,num_col),
                    ('cat_pipeline',cat_pipeline,cat_col)
                ]
            )
            logging.info('Pipeline has been completed')
            
            return preprocessor


        except Exception as exp:
            logging.info("Exception occurs in the initiate_data_transformation")
            raise customException(exp,sys)
    
    def initial_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Reading train data and test data were completed")
            logging.info(f"Train Dataframe Head:\n{train_df.head().to_string()}")
            logging.info(f"Test Dataframe Head:\n{test_df.head().to_string()}")

            preprocessor_obj=self.get_data_transformation()

            target_feature='price'
            drop_features=[target_feature,'id']

            input_feature_train_df=train_df.drop(columns=drop_features,axis=1)
            target_feature_train_df=train_df[target_feature]
            input_feature_test_df=test_df.drop(columns=drop_features,axis=1)
            target_feature_test_df=test_df[target_feature]

            input_feature_train_arr=preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessor_obj.transform(input_feature_test_df)

            logging.info('Applying column transformation on training and testing data has been completed')

            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            save_object(file_path=self.data_transformation_config.perprocessor_obj_file_path,
                        obj=preprocessor_obj)
            
            logging.info('Preprocessing pickle file saved')

            return(
                train_arr,
                test_arr
            )


        except Exception as exp:
            logging.info("Exception occurs in the initiate_data_transformation")
            raise customException(exp,sys)


from src.DimondPricePrediction.components.data_ingestion import DataIngestion
from src.DimondPricePrediction.components.data_transformation import DataTransformation
from src.DimondPricePrediction.components.model_training import ModelTraining
import pandas as pd
import numpy as np
import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exeception import customException


obj_ingestion=DataIngestion()
train_data_path,test_data_path=obj_ingestion.initiate_data_ingection()

data_transform=DataTransformation()
train_arr,test_arr=data_transform.initial_data_transformation(train_data_path,test_data_path)

model_training_obj=ModelTraining()
model_training_obj.initiat_model_training(train_arr,test_arr)

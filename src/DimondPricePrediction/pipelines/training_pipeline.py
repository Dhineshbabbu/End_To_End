from src.DimondPricePrediction.components.data_ingestion import DataIngestion
import pandas as pd
import numpy as np
import os
import sys
from src.DimondPricePrediction.logger import logging
from src.DimondPricePrediction.exeception import customException


obj_ingestion=DataIngestion()

obj_ingestion.initiate_data_ingection()
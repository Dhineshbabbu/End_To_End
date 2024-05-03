from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

custdataobj=CustomData(0.71,61.6,58.0,5.74,5.67,3.51,'Premium','F','SI2')

dataframe=custdataobj.get_data_as_dataframe()

print(dataframe)
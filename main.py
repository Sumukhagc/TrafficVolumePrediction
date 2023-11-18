from src.TrafficVolumePrediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.TrafficVolumePrediction.pipeline.data_validation_pipeline import DataValidationPipeline


try:
    data_ingestion_pipeline=DataIngestionPipeline()
    data_ingestion_pipeline.main()
except Exception as e:
    print(e)  

try:
    data_validation_pipeline=DataValidationPipeline()
    data_validation_pipeline.main()
except Exception as e:
    print(e)        


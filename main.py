from src.TrafficVolumePrediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline


try:
    data_ingestion_pipeline=DataIngestionPipeline()
    data_ingestion_pipeline.main()
except Exception as e:
    print(e)    


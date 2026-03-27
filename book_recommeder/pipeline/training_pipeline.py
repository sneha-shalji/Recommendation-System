from book_recommeder.components.stage_00_data_ingestion import DataIngestion


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()


    def start_training_pipeline(self):
        """
        starts training pipeline
        returns : none
        
        """
        self.data_ingestion.initiate_data_ingestion()
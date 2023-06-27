from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_base_model import PrepareBaseModelPipeline
from cnnClassifier.pipeline.stage_03_training import TrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import ModelEvaluationPipeline



STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Base Model Stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    base_model = PrepareBaseModelPipeline()
    base_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training Stage"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    train_model = TrainingPipeline()
    train_model.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n x=========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation"
try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
    model_eval = ModelEvaluationPipeline()
    model_eval.main()
    logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n x=========x")
except Exception as e:
    logger.exception(e)
    raise e

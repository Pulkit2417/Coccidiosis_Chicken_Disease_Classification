from cnnClassifier import logger
from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation import Evaluation


STAGE_NAME = "Model Evaluation"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        val_config = config.get_validation_config()
        evaluation = Evaluation(val_config)
        evaluation.evaluation()
        evaluation.save_score()


if __name__=="__main__":
    try:
        logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\n x=========x")
    except Exception as e:
        logger.exception(e)
        raise e
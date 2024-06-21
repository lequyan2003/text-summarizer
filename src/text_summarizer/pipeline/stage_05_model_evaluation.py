from text_summarizer.components.model_evaluation import ModelEvaluation
from text_summarizer.config.configuration import ConfigurationManager


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(
            config=model_evaluation_config
        )
        model_evaluation_config.evaluate()

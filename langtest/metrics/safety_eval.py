from typing import Dict, List, Union


class SafetyEval:
    pipeline = None

    def __init__(
        self,
        model_name: str = "meta/llamagurad-2",
        hub: str = "huggingface",
        model_kwargs: Dict[str, str] = None,
    ) -> None:
        self.model_name = model_name
        self.hub = hub
        self.model_kwargs = model_kwargs or {}

        if SafetyEval.pipeline is None:
            SafetyEval.pipeline = self.load_pipeline()

    def load_pipeline(self):
        # from transformers import pipeline

        if self.hub == "huggingface":
            from transformers import pipeline
            pipeline = pipeline("question-answering", model=model, **self.model_kwargs)
            return pipeline
        else:
            from langtest.tasks import TaskManager 

            task = TaskManager("question-answering")
            model = task.model(self.model_name, self.hub)
            return model.predict



    def evaluate_reponse(self, response: str) -> str:
        return response

    def evaluate(self, data: Union[str, List[str]]) -> str:
        return data

    def evaluate_batch(self, data: List[str]) -> List[str]:
        return data

    @staticmethod
    def reset_pipeline():
        SafetyEval.pipeline = None

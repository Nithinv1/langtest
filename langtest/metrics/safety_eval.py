from typing import Dict, List, Union


class SafetyEval:

    pipeline = None

    def __init__(
            self, 
            model_name: str = "meta/llamagurad-2",
            hub: str = "huggingface",
            model_kwargs: Dict[str, str] = None
        ) -> None:
        self.model_name = model_name
        self.hub = hub
        self.model_kwargs = model_kwargs
    
    def evaluate_reponse(self, response: str) -> str:
        return response

    def evaluate(self, data: Union[str, List[str]]) -> str:
        return data
    
    def evaluate_batch(self, data: List[str]) -> List[str]:
        return data
    
    @staticmethod
    def reset_pipeline():
        SafetyEval.pipeline = None


from sentence_transformers import CrossEncoder
from typing import List
from ._ranker import Ranker


#模型过于巨大，还是不尝试了
class BGERerankerGemma2(Ranker):
    def __init__(self,max_length:int=1024):
        from ..utils.get_sentence_device import get_sentence_transformer_device
        device = get_sentence_transformer_device()
        from ..utils.config_setting import Config
        api_key = ""
        config = Config()
        if config.has_key("hugging_face_api_key"):
            api_key = config.get("hugging_face_api_key")
        # 设置 API Key
        if api_key:
            import os
            os.environ['HUGGING_FACE_HUB_TOKEN'] = api_key
        self.model = CrossEncoder('BAAI/bge-reranker-v2.5-gemma2-lightweight',device=device,max_length=max_length,trust_remote_code=True)

    def get_scores(self, pairs:List[List[str]]) -> List[List[float]]:
        return self.model.predict(pairs) 
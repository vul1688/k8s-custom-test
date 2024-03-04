# File name: serve_quickstart.py
from starlette.requests import Request

import ray
from ray import serve




@serve.deployment(num_replicas=2, ray_actor_options={"num_cpus": 0.2, "num_gpus": 0})
class Translator:    
    def translate(self, text: str) -> str:
        return text+' hahaha'

    async def __call__(self, http_request: Request) -> str:
        english_text: str = await http_request.json()
        return self.translate(english_text)


translator_app = Translator.bind()
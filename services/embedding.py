import os
import openai

class EmbeddingModel:
    def __init__(self, api_key=None, model_name='text-embedding-ada-002'):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        openai.api_key = self.api_key
        self.model_name = model_name

    def get_embedding(self, text: str) -> list:

        response = openai.Embedding.create(
            input=text,
            model=self.model_name
        )
        return response['data'][0]['embedding']

    def get_embeddings(self, texts: list) -> list:
        response = openai.Embedding.create(
            input=texts,
            model=self.model_name
        )
        return [item['embedding'] for item in response['data']]
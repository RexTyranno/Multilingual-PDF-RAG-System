import os
from openai import OpenAI

class EmbeddingModel:
    def __init__(self, model_name='text-embedding-3-small'):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key= self.api_key)
        self.model_name = model_name

    def get_embedding(self, text: str) -> list:

        response = self.client.embeddings.create(input=text,
        model=self.model_name)
        return response.data[0].embedding

    def get_embeddings(self, texts: list) -> list:
        response = self.client.embeddings.create(input=texts,
        model=self.model_name)
        embeddings_list=[]
        for i in range (0,len(texts)):
            word_embedding= response.data[i].embedding
            embeddings_list.append(word_embedding)
            
        return embeddings_list



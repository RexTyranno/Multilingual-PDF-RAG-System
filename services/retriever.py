from services.embedding import EmbeddingModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class RetrieverService:
    def __init__(self, stored_data):
        self.stored_data = stored_data
    
    def get_relevant_context(self, query: str) -> str:
        """
        Get the most relevant context for the query
        args:
        query: str
        returns:
        context: str
        """
        query_embedding = EmbeddingModel().get_embedding(query)
        query_embedding = np.array(query_embedding).reshape(1, -1)
        stored_embeddings = np.array(self.stored_data['embedding'].tolist())
        similarity = cosine_similarity(query_embedding, stored_embeddings)
        top_5_similar_chunks = similarity.argsort()[0][::-1][:5]
        return self.stored_data.iloc[top_5_similar_chunks[0]]['Text']

      
    
    
    
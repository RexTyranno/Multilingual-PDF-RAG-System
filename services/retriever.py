from services.embedding import EmbeddingModel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class RetrieverService:
    def __init__(self, stored_data):
        self.stored_data= stored_data
    
    def get_relevant_context(self, query: str) -> str:
        
        query_embedding = EmbeddingModel().get_embedding(query)
        query_array= np.array(query_embedding)
        
        query_array_reshaped = query_array.reshape(1, -1)
        
        df= self.stored_data
    
        similarities = cosine_similarity(query_array_reshaped, df['embedding'])[0] 
    
        df = df.copy() 
        df['similarity'] = similarities
    
        k = min(k, len(df))
        
        top_k = df.nlargest(k, 'similarity')
        
        top_k_texts = top_k['Text'].tolist()
        
        context = "\n".join(top_k_texts)
        
        return context
            
      
    
    
    
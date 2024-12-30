import pandas as pd
import numpy as np

def prepare_lookup_table(chunks: str,embeddings: np.ndarray) -> str:
    
    embeddings_array= np.array(embeddings)
    
    df = pd.DataFrame({'Text': chunks,'embedding': embeddings_array})
    
    return df
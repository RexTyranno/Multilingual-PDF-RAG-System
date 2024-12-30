import pandas as pd

def prepare_lookup_table(chunks,embeddings):
    
    df = pd.DataFrame({'Text': chunks,'embedding': embeddings})
    
    return df
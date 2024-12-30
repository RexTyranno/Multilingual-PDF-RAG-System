import pandas as pd
import numpy as np

def prepare_lookup_table(chunks, embeddings):
    # Convert embeddings to a numpy array (if it's not already)
    embeddings_array = np.array(embeddings)

    # Ensure chunks is a 1-dimensional list
    if isinstance(chunks, str):  # Handle the case where chunks is a single string
        chunks = [chunks]

    # Check if lengths match
    if len(chunks) != len(embeddings_array):
        raise ValueError("Length mismatch: 'chunks' and 'embeddings' must have the same length.")

    # If embeddings is a 2D array, convert each row into a list
    if embeddings_array.ndim == 2:
        embeddings_list = [list(row) for row in embeddings_array]
    else:
        raise ValueError("Embeddings must be 2-dimensional (array of arrays).")

    # Create the DataFrame
    df = pd.DataFrame({'Text': chunks, 'embedding': embeddings_list})
    
    return df

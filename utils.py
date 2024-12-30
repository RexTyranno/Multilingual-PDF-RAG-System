import pandas as pd
import numpy as np


def prepare_lookup_table(chunks, embeddings):
    """
    Create a lookup table for the chunks and embeddings
    args:
    chunks: list of strings
    embeddings: list of arrays
    returns:
    lookup_table: pandas dataframe
    with format: {'Text': chunks, 'embedding': embeddings_list}
    """

    lookup_table = pd.DataFrame({'Text': chunks, 'embedding': embeddings})

    return lookup_table

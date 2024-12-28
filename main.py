from extraction import extract_text_digital, extract_text_scanned
from chunking import chunk_text
from storage import get_engine, init_db, store_chunks, Document
from sqlalchemy.orm import sessionmaker
from embedding import EmbeddingModel
import sys

def main(pdf_path, scanned=False, language='eng'):

    if scanned:
        extracted_text = extract_text_scanned(pdf_path, language)
    else:
        extracted_text = extract_text_digital(pdf_path)
    
    chunks = chunk_text(extracted_text, chunk_size=500)
    
    engine = get_engine()
    init_db(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    store_chunks(chunks, session)
    
    # embedding_model = EmbeddingModel()
    # for chunk in chunks[:3]:  
    #     vector = embedding_model.get_embedding(chunk)
    #     print("Chunk Embedding (first 5 dims):", vector[:5])
        
    # keyword = "example"
    # results = session.query(Document).filter(Document.text_chunk.contains(keyword)).all()
    # print(f"\nFound {len(results)} chunks containing '{keyword}':")
    # for r in results:
    #     print(r.text_chunk[:100], "...\n")

if __name__ == '__main__':
    
    pdf_path = sys.argv[1]
    scanned = False if len(sys.argv) < 3 else sys.argv[2].lower() == "true"
    lang = 'eng' if len(sys.argv) < 4 else sys.argv[3]
    
    main(pdf_path, scanned, lang)

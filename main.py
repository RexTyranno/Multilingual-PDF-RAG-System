from services.extraction import extract_text_digital, extract_text_scanned
from services.chunking import chunk_text
from services.embedding import EmbeddingModel
import sys
from dotenv import load_dotenv

load_dotenv()

def main(pdf_path, scanned=False, language='eng'):

    if scanned:
        extracted_text = extract_text_scanned(pdf_path, language)
    else:
        extracted_text = extract_text_digital(pdf_path)
    
    chunks = chunk_text(extracted_text, chunk_size=500)
    


if __name__ == '__main__':
    
    pdf_path = sys.argv[1]
    scanned = False if len(sys.argv) < 3 else sys.argv[2].lower() == "true"
    lang = 'eng' if len(sys.argv) < 4 else sys.argv[3]
    
    main(pdf_path, scanned, lang)

from services.extraction import extract_text_digital, extract_text_scanned
from services.chunking import chunk_text
from services.embedding import EmbeddingModel
from services.generator import ChatService
from utils import prepare_lookup_table
from services.retriever import RetrieverService
from dotenv import load_dotenv

load_dotenv()


def main(pdf_path, scanned=False, language='eng'):

    if scanned:
        extracted_text = extract_text_scanned(pdf_path, language)
    else:
        extracted_text = extract_text_digital(pdf_path)
    
    chunks = chunk_text(extracted_text, chunk_size=500)
    
    embeddings_obtained = EmbeddingModel().get_embeddings(chunks)
    
    lookup_table = prepare_lookup_table(chunks, embeddings_obtained)
    
    retriever = RetrieverService(lookup_table)
    
    chat_service = ChatService()

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chat_service.get_response(user_input,retriever)
        print(f"ASSISTANT: {response}")


if __name__ == '__main__':
    # pdf_path = sys.argv[1] or None
    # scanned = False if len(sys.argv) < 3 else sys.argv[2].lower() == "true"
    # lang = 'eng' if len(sys.argv) < 4 else sys.argv[3]
    
    pdf_path = "Resume_Agrima.pdf"
    scanned = False
    lang = 'eng'
    
    main(pdf_path, scanned, lang)

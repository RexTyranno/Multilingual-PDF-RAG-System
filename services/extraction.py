import pytesseract
from PIL import Image
import fitz  
import os

def extract_text_digital(pdf_path: str) -> str:

    text_content = []
    doc = fitz.open(pdf_path)
    for page in doc:
        text_content.append(page.get_text())
    return "\n".join(text_content)

def extract_text_scanned(pdf_path: str, language='eng') -> str:

    text_content = []
    doc = fitz.open(pdf_path)
    for page_idx in range(len(doc)):
        page = doc[page_idx]
        pix = page.get_pixmap()
        img_path = f"temp_page_{page_idx}.png"
        pix.save(img_path)
        
        extracted_text = pytesseract.image_to_string(Image.open(img_path), lang=language)
        text_content.append(extracted_text)

        if os.path.exists(img_path):
            os.remove(img_path)

    return "\n".join(text_content)

# ocr.py
import pytesseract
from PIL import Image

def ocr_image(image_path):
    "
    Performs OCR (Optical Character Recognition) on an image file to extract text.
    
    Args:
        image_path (str): The file path of the image to be processed.
    
    Returns:
        str: The extracted text from the image.
    "
    # Open the image file
    image = Image.open(image_path)
    
    # Use pytesseract to perform OCR on the image
    text = pytesseract.image_to_string(image)
    
    return text


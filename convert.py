# convert.py
from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path):
    "
    Converts a PDF file to a list of image files.
    
    Args:
        pdf_path (str): The file path of the PDF to be converted.
    
    Returns:
        list: A list of file paths to the converted images.
    "
    try:
        images = convert_from_path(pdf_path)
        image_files = []

        # Create output_images directory if not exists
        if not os.path.exists('output_images'):
            os.makedirs('output_images')

        # Save each page as an image file
        for i, image in enumerate(images):
            image_path = f'output_images/page_{i + 1}.jpeg'
            image.save(image_path, 'JPEG')
            image_files.append(image_path)
        return image_files
    except Exception as e:
        print(f'Error converting PDF: {e}')
        return []

from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, output):
    '''
    Merge multiple PDFs into a single PDF.
    
    Args:
        pdf_list (list): List of PDF file paths to merge.
        output (str): Path to the output merged PDF file.
    '''
    merger = PdfMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(output)
    merger.close()


# convert.py
from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path):
    try:
        images = convert_from_path(pdf_path)
        image_files = []
        if not os.path.exists('output_images'):
            os.makedirs('output_images')
        for i, image in enumerate(images):
            image_path = f'output_images/page_{i + 1}.jpeg'
            image.save(image_path, 'JPEG')
            image_files.append(image_path)
        return image_files
    except Exception as e:
        print(f'Error converting PDF: {e}')
        return []


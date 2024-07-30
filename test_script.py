# test_script.py
from convert import pdf_to_images
from ocr import ocr_image
import os

def main():
    "
    Main test function to verify the PDF to text conversion process.
    "
    pdf_path = 'test_document.pdf'  # Path to a sample test PDF
    print(f'Starting test with PDF: {pdf_path}')

    # Test PDF to images conversion
    image_files = pdf_to_images(pdf_path)
    assert len(image_files) > 0, 'No images were created from the PDF.'

    # Test OCR on the images
    for image_file in image_files:
        text = ocr_image(image_file)
        assert text is not None, 'OCR did not return any text.'

    print('All tests passed.')

if __name__ == '__main__':
    main()


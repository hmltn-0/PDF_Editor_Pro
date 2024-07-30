# test_script.py
from convert import pdf_to_images
from ocr import ocr_image

def main():
    pdf_path = '/Users/juliushamilton/apple_books_script/apple_books_interface/pdf_to_text_app/test_document.pdf'
    try:
        images = pdf_to_images(pdf_path)
        for image in images:
            text = ocr_image(image)
            print(f'Text from {image}:')
            print(text)
            print('-' * 50)
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()

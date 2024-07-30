import unittest
from convert import pdf_to_images, merge_pdfs
from ocr import ocr_image
import os

class TestPDFConverter(unittest.TestCase):
    def test_pdf_to_images(self):
        pdf_path = 'test_document.pdf'
        image_files = pdf_to_images(pdf_path)
        self.assertGreater(len(image_files), 0, 'No images were created from the PDF.')
    
    def test_ocr_image(self):
        image_path = 'output_images/page_1.jpeg'
        text = ocr_image(image_path)
        self.assertIsNotNone(text, 'OCR did not return any text.')
    
    def test_merge_pdfs(self):
        pdf_list = ['test_document.pdf', 'test_document.pdf']
        output = 'merged_output.pdf'
        merge_pdfs(pdf_list, output)
        self.assertTrue(os.path.exists(output), 'Merged PDF was not created.')

if __name__ == '__main__':
    unittest.main()


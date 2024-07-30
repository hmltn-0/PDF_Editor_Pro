# gui.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QTextEdit, QRadioButton, QButtonGroup, QLabel
from PyQt5.QtGui import QPixmap

class PDFApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PDF to Text Converter')
        self.setGeometry(100, 100, 800, 600)
        layout = QVBoxLayout()
        
        self.textEdit = QTextEdit(self)
        layout.addWidget(self.textEdit)
        
        # Radio buttons for format selection
        self.formatGroup = QButtonGroup(self)
        self.radioPlainText = QRadioButton('Plain Text', self)
        self.radioMarkdown = QRadioButton('Markdown', self)
        self.radioLatex = QRadioButton('LaTeX', self)
        self.radioPlainText.setChecked(True)  # Default to Plain Text
        layout.addWidget(self.radioPlainText)
        layout.addWidget(self.radioMarkdown)
        layout.addWidget(self.radioLatex)
        self.formatGroup.addButton(self.radioPlainText)
        self.formatGroup.addButton(self.radioMarkdown)
        self.formatGroup.addButton(self.radioLatex)

        self.btnSelect = QPushButton('Select PDF', self)
        layout.addWidget(self.btnSelect)
        self.btnSelect.clicked.connect(self.select_pdf)
        
        self.fileNameLabel = QLabel(self)
        layout.addWidget(self.fileNameLabel)
        
        self.thumbnailLabel = QLabel(self)
        layout.addWidget(self.thumbnailLabel)
        
        self.btnConvert = QPushButton('Convert to Text', self)
        layout.addWidget(self.btnConvert)
        self.btnConvert.clicked.connect(self.convert_pdf_to_text)
        
        self.setLayout(layout)

    def select_pdf(self):
        options = QFileDialog.Options()
        self.pdf_path, _ = QFileDialog.getOpenFileName(self, 'QFileDialog.getOpenFileName()', '', 'PDF Files (*.pdf)', options=options)
        if self.pdf_path:
            self.fileNameLabel.setText(f'Selected PDF: {self.pdf_path}')
            self.display_thumbnail()

    def display_thumbnail(self):
        # Display a thumbnail (first page) of the selected PDF
        pixmap = QPixmap()
        pixmap.load(self.pdf_path)
        self.thumbnailLabel.setPixmap(pixmap.scaled(200, 200, aspectRatioMode=1))

    def convert_pdf_to_text(self):
        if hasattr(self, 'pdf_path'):
            from convert import pdf_to_images
            from ocr import ocr_image
            images = pdf_to_images(self.pdf_path)
            full_text = []
            for image in images:
                text = ocr_image(image)
                formatted_text = self.format_text(text)
                full_text.append(formatted_text)
        self.textEdit.setPlainText('\n'.join(full_text))
'.join(full_text))

    def format_text(self, text):
        if self.radioPlainText.isChecked():
            return text
        elif self.radioMarkdown.isChecked():
            return self.to_markdown(text)
        elif self.radioLatex.isChecked():
            return self.to_latex(text)

    def to_markdown(self, text):
        return text

    def to_latex(self, text):
        return text

def main():
    app = QApplication(sys.argv)
    ex = PDFApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


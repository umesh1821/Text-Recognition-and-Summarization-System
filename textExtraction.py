from pytesseract import pytesseract
class textExtraction:
    def image(image):
        path=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
        pytesseract.tesseract_cmd = path
        text = pytesseract.image_to_string(image)
        return text

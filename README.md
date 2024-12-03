# Image to Text Converter

A modern **Image to Text Converter** built using Python and Tkinter. This app uses Tesseract OCR to extract text from images in multiple languages (e.g., English, Hindi, Tamil). The app features image preview, text extraction, clipboard copy, and a sleek, user-friendly interface.

---

## Install Tesseract

### Windows:
1. Download the Tesseract installer from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).
2. Install it and note the installation directory (e.g., `C:\\Program Files\\Tesseract-OCR`).
3. Configure the path in the Python script if needed:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

Linux:
sudo apt install tesseract-ocr
macOS:
bash
brew install tesseract


# Image to Text Converter

A modern **Image to Text Converter** built using Python and Tkinter. This app uses Tesseract OCR to extract text from images in multiple languages (e.g., English, Hindi, Tamil). The app features image preview, text extraction, clipboard copy, and a sleek, user-friendly interface.

---

## Install Tesseract

### Windows:
1. Download the Tesseract installer from [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract).
2. Install it and note the installation directory (e.g., `C:\Program Files\Tesseract-OCR`).
3. Configure the path in the Python script if needed:
   ```python
   pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
   ```

### Linux:
```bash
sudo apt install tesseract-ocr
```

### macOS:
```bash
brew install tesseract
```

---

## How to Use

1. Clone or download the repository to your local machine.
2. Install the required libraries as mentioned above.
3. Ensure **Tesseract-OCR** is installed and correctly configured.
4. Run the script:
   ```bash
   python image_to_text_converter.py
   ```
5. Select an image by clicking the **Select Image** button.
6. The extracted text from the image will appear in the text area.
7. You can copy the extracted text to the clipboard using the **Copy to Clipboard** button.
8. Clear the text area and image preview using the **Clear Text** button, if needed.

---

## Features

- **Image Preview**: Displays a preview of the selected image.
- **Text Extraction**: Extracts text from images using OCR in multiple languages.
- **Copy to Clipboard**: Easily copy the extracted text.
- **Language Selection**: Choose from a list of supported OCR languages.
- **Modern UI**: A user-friendly interface with hover effects and dark theme.

---

## Supported Languages

- English (`eng`)
- Hindi (`hin`)
- Tamil (`tam`)
- Sinhala (`sin`)
- French (`fra`)
- German (`deu`)
- Spanish (`spa`)
- Chinese Simplified (`chi_sim`)
- Russian (`rus`)

---

## Contributing

Contributions are welcome! Feel free to fork the repository, make changes, and submit pull requests.


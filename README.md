Image to Text Converter
A modern Image to Text Converter built using Python and Tkinter. This app uses Tesseract OCR to extract text from images in multiple languages (e.g., English, Hindi, Tamil). The app features image preview, text extraction, clipboard copy, and a sleek, user-friendly interface.
Libraries Required
To run this project, you need to install the following Python libraries:

Tkinter: For the graphical user interface.
Pillow: For image handling and preview.
Pytesseract: For Optical Character Recognition (OCR) functionality.
Tesseract-OCR: The OCR engine.

You can install the required libraries using pip:
bashCopypip install pytesseract Pillow
Additionally, Tesseract-OCR must be installed on your system. Follow the instructions for your operating system:
Install Tesseract:

Windows:

Download the Tesseract installer from this link.
Install it and note the installation directory.
Set the path to Tesseract in your code (or environment variables).

Example (Windows):
pythonCopypytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

Linux:
bashCopysudo apt install tesseract-ocr

macOS:
bashCopybrew install tesseract


How to Use

Clone or download the repository to your local machine.
Install the required libraries as mentioned above.
Make sure Tesseract-OCR is installed and correctly configured.
Run the script:
bashCopypython image_to_text_converter.py

Select an image by clicking the Select Image button.
The extracted text from the image will appear in the text area.
You can copy the extracted text to the clipboard using the Copy to Clipboard button.
If needed, clear the text area and image preview using the Clear Text button.

Features

Image Preview: Displays a preview of the selected image.
Text Extraction: Extracts text from the image using OCR in multiple languages.
Copy to Clipboard: Allows you to copy the extracted text to your clipboard.
Language Selection: Choose the OCR language from a dropdown.

Contributing
Feel free to fork the repository, make changes, and submit pull requests.

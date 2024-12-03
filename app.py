import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from tkinter import PhotoImage
import pytesseract
from PIL import Image, ImageTk
import os


class ModernOCRImageTextExtractor:
    def __init__(self, master):
        # Set up main window
        self.master = master
        master.title("Modern OCR Image Text Extractor")
        master.geometry("850x750")
        master.configure(bg="#1C2833")  # Darker, sleek background

        # Set custom fonts
        self.title_font = ("Segoe UI", 20, "bold")
        self.label_font = ("Roboto", 12)
        self.button_font = ("Roboto", 12, "bold")

        # Create styled widgets
        self.create_widgets()

    def create_widgets(self):
        # Title Frame
        title_frame = tk.Frame(self.master, bg="#1C2833")
        title_frame.pack(pady=(20, 10))

        # Title Label
        title_label = tk.Label(
            title_frame,
            text="Modern OCR Image Text Extractor",
            font=self.title_font,
            bg="#1C2833",
            fg="#F1C40F"
        )
        title_label.pack()

        # Icon (Optional, replace 'icon.png' with your own image)
        try:
            self.icon = PhotoImage(file="icon.png")
            icon_label = tk.Label(title_frame, image=self.icon, bg="#1C2833")
            icon_label.pack(pady=5)
        except:
            pass  # If no icon file exists, continue without error

        # Image Frame
        image_frame = tk.Frame(self.master, bg="#1C2833")
        image_frame.pack(pady=15)

        self.image_preview = tk.Label(
            image_frame,
            text="No Image Selected",
            font=self.label_font,
            bg="#34495E",
            fg="#ECF0F1",
            width=50,
            height=15,
            relief=tk.SUNKEN
        )
        self.image_preview.pack()

        # Buttons Frame
        buttons_frame = tk.Frame(self.master, bg="#1C2833")
        buttons_frame.pack(pady=10)

        # Select Image Button
        self.select_button = tk.Button(
            buttons_frame,
            text="Select Image",
            command=self.select_image,
            font=self.button_font,
            bg="#3498DB",
            fg="white",
            activebackground="#2980B9",
            relief=tk.FLAT,
            padx=15,
            pady=8
        )
        self.select_button.pack(side=tk.LEFT, padx=10)

        # Clear Image Button
        self.clear_button = tk.Button(
            buttons_frame,
            text="Clear Image",
            command=self.clear_image_preview,
            font=self.button_font,
            bg="#E74C3C",
            fg="white",
            activebackground="#C0392B",
            relief=tk.FLAT,
            padx=15,
            pady=8
        )
        self.clear_button.pack(side=tk.LEFT)

        # Language Selection Frame
        language_frame = tk.Frame(self.master, bg="#1C2833")
        language_frame.pack(pady=10)

        # Language Dropdown Label
        language_label = tk.Label(
            language_frame,
            text="Select OCR Language:",
            font=self.label_font,
            bg="#1C2833",
            fg="#ECF0F1"
        )
        language_label.pack(side=tk.LEFT, padx=(0, 10))

        # Language Dropdown
        self.language_var = tk.StringVar(value="eng")
        self.language_options = ["eng", "hin", "tam", "sin", "fra", "deu", "spa", "chi_sim", "rus"]
        self.language_dropdown = ttk.Combobox(
            language_frame,
            textvariable=self.language_var,
            values=self.language_options,
            state="readonly",
            font=self.label_font,
            width=15
        )
        self.language_dropdown.pack(side=tk.LEFT)

        # Text Display Area
        self.text_area = scrolledtext.ScrolledText(
            self.master,
            wrap=tk.WORD,
            width=80,
            height=15,
            font=("Consolas", 11),
            bg="#273746",
            fg="#ECF0F1",
            insertbackground="white",
            relief=tk.GROOVE
        )
        self.text_area.pack(pady=15)

        # Footer Buttons Frame
        footer_buttons_frame = tk.Frame(self.master, bg="#1C2833")
        footer_buttons_frame.pack(pady=10)

        # Copy to Clipboard Button
        self.copy_button = tk.Button(
            footer_buttons_frame,
            text="Copy Text",
            command=self.copy_to_clipboard,
            font=self.button_font,
            bg="#2ECC71",
            fg="white",
            activebackground="#27AE60",
            relief=tk.FLAT,
            padx=15,
            pady=8
        )
        self.copy_button.pack(side=tk.LEFT, padx=10)

        # Clear Text Button
        self.clear_text_button = tk.Button(
            footer_buttons_frame,
            text="Clear Text",
            command=self.clear_text,
            font=self.button_font,
            bg="#E74C3C",
            fg="white",
            activebackground="#C0392B",
            relief=tk.FLAT,
            padx=15,
            pady=8
        )
        self.clear_text_button.pack(side=tk.LEFT)

        # Add hover effects
        self.add_hover_effects()

    def add_hover_effects(self):
        def on_enter(widget, color):
            widget.config(bg=color)

        def on_leave(widget, original_color):
            widget.config(bg=original_color)

        # Hover effects for buttons
        buttons = [
            (self.select_button, "#2980B9", "#3498DB"),
            (self.clear_button, "#C0392B", "#E74C3C"),
            (self.copy_button, "#27AE60", "#2ECC71"),
            (self.clear_text_button, "#C0392B", "#E74C3C")
        ]

        for button, hover_color, original_color in buttons:
            button.bind("<Enter>", lambda e, b=button, c=hover_color: on_enter(b, c))
            button.bind("<Leave>", lambda e, b=button, c=original_color: on_leave(b, c))

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff"), ("All files", "*.*")])
        if not file_path:
            return

        try:
            image = Image.open(file_path)
            preview_image = image.copy()
            preview_image.thumbnail((400, 300))
            photo = ImageTk.PhotoImage(preview_image)

            self.image_preview.configure(image=photo, text="")
            self.image_preview.image = photo

            text = pytesseract.image_to_string(image, lang=self.language_var.get())
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, text)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def clear_image_preview(self):
        self.image_preview.configure(image='', text="No Image Selected")
        self.image_preview.image = None

    def copy_to_clipboard(self):
        text = self.text_area.get(1.0, tk.END).strip()
        if text:
            self.master.clipboard_clear()
            self.master.clipboard_append(text)
            messagebox.showinfo("Success", "Text copied to clipboard!")

    def clear_text(self):
        self.text_area.delete(1.0, tk.END)


def main():
    root = tk.Tk()
    app = ModernOCRImageTextExtractor(root)
    root.mainloop()


if __name__ == "__main__":
    main()

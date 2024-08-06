import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps

class ImageEditorApp:
    def __init__(self, root):  # Corrigido de _init_ para __init__
        self.root = root
        self.root.title("Image Editor")

        # Layout setup
        self.frame_left = tk.Frame(root, width=200, height=400, padx=10, pady=10)
        self.frame_left.grid(row=0, column=0, sticky="ns")

        self.frame_right = tk.Frame(root, width=600, height=400, padx=10, pady=10)
        self.frame_right.grid(row=0, column=1, sticky="nsew")

        # Imagem Original
        self.label_original = tk.Label(self.frame_left, text="Original Image")
        self.label_original.pack()

        self.canvas_original = tk.Canvas(self.frame_left, width=180, height=180, bg='gray')
        self.canvas_original.pack(pady=10)

        # Seleção de filtros
        self.label_filters = tk.Label(self.frame_left, text="Select between various tools or filters")
        self.label_filters.pack()

        self.filters = [
            "BLUR", "CONTOUR", "DETAIL", "EDGE_ENHANCE", "EMBOSS", "SHARPEN",
            "SOLARIZE", "POSTERIZE", "COLORIZE", "INVERT", "SEPIA"
        ]
        self.filter_combobox = ttk.Combobox(self.frame_left, values=self.filters)
        self.filter_combobox.pack(pady=10)
        self.filter_combobox.bind("<<ComboboxSelected>>", self.apply_filter)

        self.button_upload = tk.Button(self.frame_left, text="Upload Image", command=self.upload_image)
        self.button_upload.pack(pady=20)

        # Image (Large) Area para mostrar a imagem editada
        self.canvas_large = tk.Canvas(self.frame_right, width=500, height=400, bg='white')
        self.canvas_large.pack()

        self.image = None
        self.photo = None

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.display_image(self.image)

    def display_image(self, image):
        self.photo = ImageTk.PhotoImage(image.resize((180, 180)))
        self.canvas_original.create_image(90, 90, image=self.photo)

        self.photo_large = ImageTk.PhotoImage(image.resize((500, 400)))
        self.canvas_large.create_image(250, 200, image=self.photo_large)

    def apply_filter(self, event):
        if self.image:
            filter_name = self.filter_combobox.get()
            if filter_name == "BLUR":
                filtered_image = self.image.filter(ImageFilter.BLUR)
            elif filter_name == "CONTOUR":
                filtered_image = self.image.filter(ImageFilter.CONTOUR)
            elif filter_name == "DETAIL":
                filtered_image = self.image.filter(ImageFilter.DETAIL)
            elif filter_name == "EDGE_ENHANCE":
                filtered_image = self.image.filter(ImageFilter.EDGE_ENHANCE)
            elif filter_name == "EMBOSS":
                filtered_image = self.image.filter(ImageFilter.EMBOSS)
            elif filter_name == "SHARPEN":
                filtered_image = self.image.filter(ImageFilter.SHARPEN)
            elif filter_name == "SOLARIZE":
                filtered_image = ImageOps.solarize(self.image, threshold=128)
            elif filter_name == "POSTERIZE":
                filtered_image = ImageOps.posterize(self.image, bits=4)
            elif filter_name == "COLORIZE":
                filtered_image = ImageOps.colorize(self.image.convert("L"), black="blue", white="yellow")
            elif filter_name == "INVERT":
                filtered_image = ImageOps.invert(self.image.convert("RGB"))
            elif filter_name == "SEPIA":
                sepia_image = self.image.convert("L")
                sepia_image = ImageOps.colorize(sepia_image, black="brown", white="yellow")
                filtered_image = sepia_image

            self.display_image(filtered_image)

root = tk.Tk()
app = ImageEditorApp(root)
root.mainloop()
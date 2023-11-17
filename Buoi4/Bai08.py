import cv2
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageBorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Thay Đổi Biên Ảnh")

        # Tạo các biến
        self.image_path = None
        self.border_size = 5

        # Tạo các widgets
        self.label = tk.Label(root, text="Chọn ảnh:")
        self.label.pack(pady=10)

        self.canvas = tk.Canvas(root, width=300, height=300)
        self.canvas.pack()

        self.choose_button = tk.Button(root, text="Chọn ảnh", command=self.choose_image)
        self.choose_button.pack(pady=10)

        self.slider_label = tk.Label(root, text="Kích thước biên:")
        self.slider_label.pack()
        self.border_slider = tk.Scale(root, from_=1, to=20, orient=tk.HORIZONTAL, length=200, command=self.update_border_size)
        self.border_slider.set(self.border_size)
        self.border_slider.pack()

        self.process_button = tk.Button(root, text="Thay đổi biên ảnh", command=self.process_image)
        self.process_button.pack(pady=10)

    def choose_image(self):
        self.image_path = filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if self.image_path:
            self.display_image()

    def display_image(self):
        image = Image.open(self.image_path)
        image.thumbnail((300, 300))
        photo = ImageTk.PhotoImage(image)
        self.canvas.config(width=photo.width(), height=photo.height())
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def update_border_size(self, value):
        self.border_size = int(value)

    def process_image(self):
        if self.image_path:
            original_image = cv2.imread(self.image_path)
            bordered_image = cv2.copyMakeBorder(original_image, self.border_size, self.border_size, self.border_size, self.border_size, cv2.BORDER_CONSTANT, value=[255, 255, 255])

            cv2.imshow("Bordered Image", bordered_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageBorderApp(root)
    root.mainloop()

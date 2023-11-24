import cv2
import numpy as np
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog

def enhance_image(image_path):
    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)

    # Chuyển đổi ảnh sang không gian màu LAB
    lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Phân tách kênh L, a, b
    l, a, b = cv2.split(lab)

    # Áp dụng phép cân bằng histogram cho kênh L
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    enhanced_l = clahe.apply(l)

    # Ghép lại các kênh L, a, b
    enhanced_lab = cv2.merge((enhanced_l, a, b))

    # Chuyển đổi ảnh lại sang không gian màu BGR
    enhanced_image = cv2.cvtColor(enhanced_lab, cv2.COLOR_LAB2BGR)

    return enhanced_image

def open_image():
    # Mở hộp thoại chọn file ảnh
    image_path = tk.filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    if image_path:
        # Tăng cường chất lượng ảnh
        enhanced_image = enhance_image(image_path)

        # Hiển thị ảnh gốc
        original_img = Image.open(image_path)
        original_img.thumbnail((400, 400))
        original_img = ImageTk.PhotoImage(original_img)
        original_label.configure(image=original_img)
        original_label.image = original_img

        # Hiển thị ảnh được tăng cường
        enhanced_img = cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB)
        enhanced_img = Image.fromarray(enhanced_img)
        enhanced_img.thumbnail((400, 400))
        enhanced_img = ImageTk.PhotoImage(enhanced_img)
        enhanced_label.configure(image=enhanced_img)
        enhanced_label.image = enhanced_img

# Tạo cửa sổ giao diện sử dụng Tkinter
window = tk.Tk()
window.title("Enhance Image")

# Tạo nút "Open Image" để chọn ảnh
open_button = tk.Button(window, text="Open Image", command=open_image)
open_button.pack()

# Tạo hai nhãn để hiển thị ảnh gốc và ảnh được tăng cường
original_label = tk.Label(window)
original_label.pack(side=tk.LEFT)
enhanced_label = tk.Label(window)
enhanced_label.pack(side=tk.RIGHT)

# Chạy chương trình
window.mainloop()

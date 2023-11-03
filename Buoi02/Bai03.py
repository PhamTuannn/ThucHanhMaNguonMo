import tkinter as tk
import numpy as np
import math

def hinhtron():
    def calculate_circle():
        side_length = float(entry_side_length.get())
        area = side_length * math.pi ** 2
        perimeter = 2 * side_length * math.pi
        label_area.config(text="Diện tích: {:.2f}".format(area))
        label_perimeter.config(text="Chu vi: {:.2f}".format(perimeter))
    A = tk.Tk()
    A.title("Hỗ trợ hình tròn")
    A.geometry("300x200")
    label_side_length = tk.Label(A, text="Độ dài bán kính R:")
    label_side_length.pack()
    entry_side_length = tk.Entry(A)
    entry_side_length.pack()
    button_calculate = tk.Button(A, text="Tính toán", command=calculate_circle)
    button_calculate.pack()
    label_area = tk.Label(A, text="Diện tích:")
    label_area.pack()
    label_perimeter = tk.Label(A, text="Chu vi:")
    label_perimeter.pack()
    A.mainloop()

def hinhvuong():
    def calculate_square():
        lenth = float(entry_side_length.get())
        area = lenth ** 2
        perimeter = 4 * lenth
        label_area.config(text="Diện tích: {:.2f}".format(area))
        label_perimeter.config(text="Chu vi: {:.2f}".format(perimeter))
    B = tk.Tk()
    B.title("Hỗ trợ hình vuông")
    B.geometry("300x200")
    label_side_length = tk.Label(B, text="Độ dài cạnh:")
    label_side_length.pack()
    entry_side_length = tk.Entry(B)
    entry_side_length.pack()
    button_calculate = tk.Button(B, text="Tính toán", command=calculate_square)
    button_calculate.pack()
    label_area = tk.Label(B, text="Diện tích:")
    label_area.pack()
    label_perimeter = tk.Label(B, text="Chu vi:")
    label_perimeter.pack()
    B.mainloop()

def hinhchunhat():
    def calculate_rectangle():
        lenth = float(entry_side_length.get())
        width = float(entry_side_width.get())
        area = lenth * width
        perimeter = (lenth + width) * 2
        label_area.config(text="Diện tích: {:.2f}".format(area))
        label_perimeter.config(text="Chu vi: {:.2f}".format(perimeter))
    C = tk.Tk()
    C.title("Hỗ trợ hình chữ nhật")
    C.geometry("300x200")
    label_side_length = tk.Label(C, text="Độ dài chiều dài và chiều rộng:")
    label_side_length.pack()
    entry_side_length = tk.Entry(C)
    entry_side_length.pack()
    entry_side_width = tk.Entry(C)
    entry_side_width.pack()
    button_calculate = tk.Button(C, text="Tính toán", command=calculate_rectangle)
    button_calculate.pack()
    label_area = tk.Label(C, text="Diện tích:")
    label_area.pack()
    label_perimeter = tk.Label(C, text="Chu vi:")
    label_perimeter.pack()
    C.mainloop()
# Tạo giao diện
window = tk.Tk()
window.title("Hỗ trợ học tập môn hình học")
window.geometry("300x200")

# Tạo các thành phần giao diện
label_side_length = tk.Label(window, text="Chọn hình bạn muốn hỗ trợ")
label_side_length.pack()

bt_hinhtron = tk.Button(window, text="Hình tròn", command=hinhtron)
bt_hinhtron.pack()

bt_hinhvuong = tk.Button(window, text="Hình vuông", command=hinhvuong)
bt_hinhvuong.pack()

bt_hinhchunhat = tk.Button(window, text="Hình chữ nhật", command=hinhchunhat)
bt_hinhchunhat.pack()

# Chạy chương trình
window.mainloop()

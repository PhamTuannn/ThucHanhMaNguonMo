import numpy as np
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from scipy.fft import fft


def process_signal():
    frequency = float(frequency_entry.get())
    t = np.linspace(0, 1, 1000)
    signal = np.sin(2 * np.pi * frequency * t)

    ax.clear()
    ax.plot(t, signal)
    ax.set_title(f'Tín hiệu với tần số {frequency} Hz')

    # Tính và hiển thị biểu diễn phổ
    sp = np.fft.fft(signal)
    freq = np.fft.fftfreq(len(signal), t[1] - t[0])
    ax_spectrum.clear()
    ax_spectrum.plot(freq, np.abs(sp))
    ax_spectrum.set_title('Biểu diễn Phổ')

    canvas.draw()


root = tk.Tk()
root.title("Xử lý Tín hiệu số")
root.geometry("800x600")

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(211)
ax_spectrum = fig.add_subplot(212)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

entry_label = ttk.Label(root, text="Nhập tần số:")
entry_label.pack()

frequency_entry = ttk.Entry(root)
frequency_entry.pack()

process_button = ttk.Button(root, text="Xử lý Tín hiệu", command=process_signal)
process_button.pack()

root.mainloop()

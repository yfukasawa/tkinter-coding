import tkinter as tk
import time

window_width  = 700
window_height = 500

def main():
    window = tk.Tk()
    window.geometry("%dx%d" % (window_width, window_height))

    # Windowのタイトル
    window.title("GUI")

    label = tk.Label(window, text="Hello World!")
    label.place(x=0, y=0)

    window.mainloop()

if __name__ == "__main__":
    main()

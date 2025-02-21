import tkinter as tk
from process_page import process_page
from reconstructed_page import reconstructed_page
from recurrence_page import recurrence_page
import numpy as np
import os

# root file for the tkinter window
# manages all changes in frame

class root(tk.Tk):
    def __init__(self):
        super().__init__()

        pages = (process_page, reconstructed_page, recurrence_page)

        # global variables
        self.controller = self
        self.df = self.load_data()
        self.recons = None
        self.reconstructed_data = None
        self.recurrence_data = None
        self.title("CSV Analyzer")
        self.geometry("700x500")
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.frames = {}

        for F in pages:
            frame = F(self.container, self)
            print(frame)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("process_page")

    def show_frame(self, frame_class):
        print("changing frame to: " + frame_class)

        if frame_class == "process_page":
            frame_class = process_page
        elif frame_class == "reconstructed_page":
            frame_class = reconstructed_page
        elif frame_class == "recurrence_page":
            frame_class = recurrence_page

        frame = self.frames[frame_class]
        frame.tkraise()  

    # customize function to load data into nparray
    def load_data(self):
        current = os.path.abspath(__file__)
        root_dir = os.path.dirname(current)
        last = os.path.basename(root_dir)

        # print("cheese: " + last)
        # pass
        print("loading file")
        # return np.loadtxt(f"{last}/csv_files/DailyDelhiClimateTest.csv", delimiter=",", skiprows=1, usecols=2)
        return np.loadtxt("csv_files/DailyDelhiClimateTrain.csv", delimiter=",", skiprows=1, usecols=2)


if __name__ == "__main__":
    app = root()
    app.mainloop()
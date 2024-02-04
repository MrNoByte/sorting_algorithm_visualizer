import tkinter as tk
from tkinter import ttk
from bubble_sort import BubbleSort
from constants import SCR_HEIGHT, SCR_WIDTH, SCREEN_MIN_HEIGHT_LIMIT, SCREEN_MIN_WIDTH_LIMIT

from home_screen import HomeScreen
from navigator import Navigator
from visualizer_screen import VisualizerScreen




root = tk.Tk()
root.title("SAV")
root.geometry(f"{SCR_WIDTH}x{SCR_HEIGHT}")
root.minsize(SCREEN_MIN_WIDTH_LIMIT,SCREEN_MIN_HEIGHT_LIMIT)

navigator = Navigator(root)

# home = HomeScreen(root)
# home.pack()


navigator.addFrame("home",HomeScreen(root,navigator))
navigator.addFrame("visualize",BubbleSort(root, navigator))
# navigator.showPage("home")


root.mainloop()



import tkinter as tk
from home_screen import HomeScreen
from bubble_sort import BubbleSort
from insertion_sort import InsertionSort
from merge_sort import MergeSort
from quick_sort import QuickSort
from constants import SCR_HEIGHT, SCR_WIDTH, SCREEN_MIN_HEIGHT_LIMIT, SCREEN_MIN_WIDTH_LIMIT
from navigator import Navigator
from selection_sort import SelectionSort
from visualizer_screen import VisualizerScreen
from constants import *

root = tk.Tk()
root.title("SAV")
root.geometry(f"{SCR_WIDTH}x{SCR_HEIGHT}")
root.minsize(SCREEN_MIN_WIDTH_LIMIT, SCREEN_MIN_HEIGHT_LIMIT)

navigator = Navigator(root)

navigator.addFrame(KEY_HOME, HomeScreen)
navigator.addFrame(KEY_BUBBLE_SORT, BubbleSort)
navigator.addFrame(KEY_INSERTION_SORT, InsertionSort)
navigator.addFrame(KEY_MERGE_SORT, MergeSort)
navigator.addFrame(KEY_QUICK_SORT, QuickSort)
navigator.addFrame(KEY_SELECTION_SORT,SelectionSort)
# navigator.addFrame("visualize", VisualizerScreen(root, navigator, "Visualize"))  # Add Visualize frame
# navigator.showPage("home")

root.mainloop()

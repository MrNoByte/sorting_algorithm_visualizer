from constants import ALGO_DELAY_MS
from visualizer_screen import VisualizerScreen
import time 

class BubbleSort(VisualizerScreen):
    def __init__(self, parent, navigator):
        super().__init__(parent, navigator, "Bubble Sort")
        self.parent = parent
        
    def on_start_click(self):
        self.bubble_sort(0)
        
    def bubble_sort(self, i):
        if i < self.length - 1:
            for j in range(0, self.length - i - 1):
                if self.array[j] > self.array[j + 1]:
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    self.drawArray()
        self.after(ALGO_DELAY_MS, self.bubble_sort, i + 1)  # Schedule the next iteration
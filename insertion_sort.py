from visualizer_screen import VisualizerScreen


class InsertionSort(VisualizerScreen):

    def __init__(self, parent, navigator):
        super().__init__(parent, navigator, "Insertion Sort")
        self.parent = parent

    def on_start_click(self):
        self.bubble_sort(0)

    def insertion_sort(self,i):
        pass
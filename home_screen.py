import tkinter as tk
from tkinter import ttk


class HomeScreen(tk.Frame):
    
    navigator = None 
    def __init__(self, parent,navigator):
        super().__init__(parent)
        self.navigator = navigator

        
        tk.Label(self, text= "Welcome Geek!",font=('Roman',40)).pack(padx=10,pady=10)
        tk.Label(self,text="Select One Algorithm to visualize.").pack()
        tk.Label(self).pack(pady=4)
        fr = tk.Frame(self)



        btn = ttk.Button(fr,text="Bubble Sort",padding=(20,20),command=lambda:navigator.showPage('visualize'))
        btn.grid(row=0,column=0)

        tk.Label(fr, text="Label inside Grid").grid(row=0,column=1)
        fr.pack()
        # self.pack(padx=11,pady=15)


#  # Create a style
#         self.style = ttk.Style()

#         

#         # Create a themed button using ttk.Button
#         styled_button = ttk.Button(self, text="Styled Button", command=self.on_button_click)
#         styled_button.pack(padx=20, pady=20)

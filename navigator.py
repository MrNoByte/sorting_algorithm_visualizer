
class Navigator:
    current_page = None

    def __init__(self,root):
        self.root = root
        self.screens = {}

    def addFrame(self, key,screen):
        self.screens[key] = screen
        if self.current_page == None:
            screen.pack()
            self.current_page = screen

    def showPage(self,key):
        if self.current_page:
            self.current_page.pack_forget()
        
        self.screens[key].pack()
        self.current_page = self.screens[key]
        
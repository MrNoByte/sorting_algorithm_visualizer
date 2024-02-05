class Navigator:
    current_page = None

    def __init__(self,root):
        self.root = root
        self.screens = {}

    def addFrame(self, key, screen_class):
        self.screens[key] = screen_class
        if self.current_page == None:
            self.showPage(key)

    def showPage(self, key):
        if self.current_page:
            self.current_page.destroy()

        screen_class = self.screens[key]
        self.current_page = screen_class(self.root, self)
        self.current_page.pack()

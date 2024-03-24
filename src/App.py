import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.width = 500
        self.height = 500
        self.screens = {}
        self.geometry(f"{self.width}x{self.height}")
        self.title("Generador de árboles 🌲")
        ctk.set_appearance_mode("system")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
    
    def show_screen(self, container):
        for s in self.screens:
            s.grid_remove(self)
            
        screen = self.screens[container]
        screen.show()

    def default_screen(self, Screen): 
      self.add_screen(Screen)
      self.show_screen(Screen)

    def add_screen(self, Screen):
        screen = Screen(self, self)
        self.screens[Screen] = screen

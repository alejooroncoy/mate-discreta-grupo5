import customtkinter as ctk

class Screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0, fg_color="transparent")
        self.controller = controller

    def show(self):
        self.grid(row=0, column=0, sticky="nsew")

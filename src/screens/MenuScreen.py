from bases.Screen import Screen
import customtkinter as ctk
import sys
from utils.fonts import getFont
# from tkextrafont


class MenuScreen(Screen):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.paint()
        
    def paint(self):
        
        title = ctk.CTkLabel(self, text="Tree generator", font=getFont(size=50, weight="bold"  ))
        title.pack(anchor=ctk.N, pady=60)
        
        containerButtons = ctk.CTkFrame(self, fg_color="transparent")
        containerButtons.pack(side=ctk.LEFT, padx=40, anchor=ctk.N, pady=20)
        
        button_tree = ctk.CTkButton(containerButtons, text="Generar árbol", command=lambda: self.controller.show_screen("TreeScreen"), font=getFont(size=13), height=30)
        button_tree.pack(pady=10)

        
        button_instructions = ctk.CTkButton(containerButtons, text="Instrucciones", command=lambda: self.controller.show_screen("InstructionsScreen"), font=getFont(size=13), height=30)
        button_instructions.pack(pady=10)

        button_credits = ctk.CTkButton(containerButtons, text="Créditos", command=lambda: self.controller.show_screen("CreditsScreen"), font=getFont(size=13), height=30)
        button_credits.pack(pady=10)
        

        button_leave = ctk.CTkButton(containerButtons, text="Salir", command=lambda: sys.exit(),  font=getFont(size=13), height=30);
        button_leave.pack(pady=10)
    

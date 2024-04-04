from bases.Screen import Screen
import customtkinter as ctk
import tkinter
from utils.fonts import getFont
from libs.trees import create_tree

class TreeScreen(Screen):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

    def load(self):
        tree = create_tree()
        print(tree)
        
    def paint(self):
        label_info = ctk.CTkLabel(self, text="R={}...",font=getFont(size=20, weight="bold"))
        label_info.pack(pady=10, padx=10)

        frame_options = ctk.CTkFrame(self, fg_color="transparent")
        frame_options.pack(side="right", expand=True, padx=0, pady=20)

        btn1 = ctk.CTkButton(frame_options, text="Crear arbol binario")
        btn1.grid(row=0, column=0, padx=10, pady=10)

        btn2 = ctk.CTkButton(frame_options, text="Crear tabla \nLEFT-VALUE-RIGHT")
        btn2.grid(row=1, column=0, padx=10, pady=10)

        btn3 = ctk.CTkButton(frame_options, text="Crear nuevo arbol")
        btn3.grid(row=2, column=0, padx=10, pady=10)

        btn4 = ctk.CTkButton(frame_options, text="Regresar al menu", command=lambda: self.controller.show_screen("MenuScreen"))
        btn4.grid(row=3, column=0, padx=10, pady=10)

        canvas=tkinter.Canvas(self, width=500, height=300)
        canvas.pack(side="right", padx=20, pady=20)

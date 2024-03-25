from bases.Screen import Screen
import customtkinter as ctk
import sys

class MenuScreen(Screen):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.paint()
        
    def paint(self):
        # Aquí viene
        button_tree = ctk.CTkButton(self,text="Generar árbol");
        button_tree.place(relx =0.5, rely=0.5, anchor=ctk.CENTER)
        button_tree.pack(padx=10, pady=10)

        button_instructions = ctk.CTkButton(self,text="Instrucciones");
        button_instructions.place(relx =0.5, rely=0.4, anchor=ctk.CENTER)
        button_instructions.pack(padx=10, pady=10)

        button_credits = ctk.CTkButton(self,text="Créditos");
        button_credits.place(relx =0.5, rely=0.3, anchor=ctk.CENTER)
        button_credits.pack(padx=10, pady=10)

        button_leave = ctk.CTkButton(self,text="Salir", command=lambda: sys.exit());
        button_leave.place(relx =0.5, rely=0.2, anchor=ctk.CENTER)
        button_leave.pack(padx=10, pady=10)
from bases.Screen import Screen
import customtkinter as ctk

class CreditsScreen(Screen):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
    def paint(self):
        longtext = """Colocar Creditos"""

        title_label = ctk.CTkLabel(self, text="Créditos", font=ctk.CTkFont(size=30, weight="bold"))
        title_label.pack(padx=10, pady=(40, 20))


        scroll_frame = ctk.CTkScrollableFrame(self, width=200, height=300)
        scroll_frame.pack(padx=10, pady=10)

        label_1 = ctk.CTkLabel(scroll_frame, text=longtext)
        label_1.pack()

        button_back = ctk.CTkButton(self,text="Volver", command=lambda: self.controller.show_screen("MenuScreen"));
        button_back.pack(padx=10, pady=10)
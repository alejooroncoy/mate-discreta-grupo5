from bases.Screen import Screen
import customtkinter as ctk

class InstructionsScreen(Screen):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
    def paint(self):
        longtext = """Uso del programa:
        1. Generar Árbol:
        - Esta opcion te abrira una pantalla que te generar un arbol a partir de las reglas especificas del algoritmo utilizado.
        Estas reglas son:
        (Introducir las reglas)

        2. Instrucciones:
        - Al seleccionar esta opcion, podras vizualisar las instrucciones importantes sobre como utilizar las funcionalidades del programa.

        3. Creditos:
        - En esta opcion, podras ver los desarrolladores que contribuieron con el proyecto.

        4. Salir:
        - Opcion para finalizar el programa."""

        title_label = ctk.CTkLabel(self, text="Instrucciones", font=ctk.CTkFont(size=30, weight="bold"))
        title_label.pack(padx=10, pady=(40, 20))


        scroll_frame = ctk.CTkScrollableFrame(self, width=200, height=300)
        scroll_frame.pack(padx=10, pady=10)

        label_1 = ctk.CTkLabel(scroll_frame, text=longtext)
        label_1.pack()

        button_back = ctk.CTkButton(self,text="Volver", command=lambda: self.controller.show_screen("MenuScreen"));
        button_back.pack(padx=10, pady=10)
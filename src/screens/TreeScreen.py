from bases.Screen import Screen
import customtkinter as ctk
from screens.BinaryScreen import BinaryScreen
from utils.fonts import getFont
from random import random
from PIL import Image
from libs.trees import create_tree, tree_for_extension
from anytree.exporter import UniqueDotExporter
from utils.createFolder import create_folder

class TreeScreen(Screen):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
    def generate_path_tree(self):
        return f"./tree-pro/tree-pro-{hash(random() * 10.0)}.png"
    
    def load(self):
        create_folder()
        self.tree = create_tree()
        self.path_tree = self.generate_path_tree()
        
        UniqueDotExporter(self.tree).to_picture(self.path_tree)
        
    def change_to_binary(self):
        # self.tree = create_tree()
        # n_tree_binary(self.tree)
        self.binaryScreen = BinaryScreen(self.controller, self.tree)
        # self.binaryScreen.focus()
    

    def create_new_tree(self):
        self.tree = create_tree()
        self.update()
        
    def paint(self):
        
        for_extension = tree_for_extension(self.tree)
        
        container = ctk.CTkFrame(self, fg_color="transparent")
        
        self.label_t = ctk.CTkLabel(container, text=f"Árbol T-{self.tree.get_n()}", font=getFont(size=25, weight="bold"))
        self.label_t.pack(pady=5, padx=10)
        
        self.label_info = ctk.CTkLabel(container, text=for_extension,font=getFont(size=20, weight="bold"), wraplength=self.controller.winfo_reqwidth() - 70)
        self.label_info.pack(pady=10, padx=10)
        
        frame_options = ctk.CTkFrame(container, fg_color="transparent")
        frame_options.pack(side="right", expand=True, padx=0, pady=20)

        self.image_tree = ctk.CTkImage(light_image=Image.open(self.path_tree), dark_image=Image.open(self.path_tree), size=(155 * 16 / 9, 160 * 16 / 9))
        
        self.image = ctk.CTkLabel(container, image=self.image_tree, text="")
        self.image.pack(side="left", padx=20, pady=0)
        
        btn1 = ctk.CTkButton(frame_options, text="Crear arbol binario", command=self.change_to_binary)
        btn1.grid(row=0, column=0, padx=10, pady=10)

        btn2 = ctk.CTkButton(frame_options, text="Crear tabla \nLEFT-VALUE-RIGHT")
        btn2.grid(row=1, column=0, padx=10, pady=10)

        btn3 = ctk.CTkButton(frame_options, text="Crear nuevo arbol", command=self.create_new_tree)
        btn3.grid(row=2, column=0, padx=10, pady=10)

        btn4 = ctk.CTkButton(frame_options, text="Regresar al menu", command=lambda: self.controller.show_screen("MenuScreen"))
        btn4.grid(row=3, column=0, padx=10, pady=10)
        
        container.pack(expand=True, pady= 20)
        
    def update(self):
        for_extension = tree_for_extension(self.tree)
        self.label_info.configure(text=for_extension)
        self.label_t.configure(text=f"Árbol T-{self.tree.get_n()}")
        
        self.path_tree = self.generate_path_tree()
        UniqueDotExporter(self.tree).to_picture(self.path_tree)
        
        self.image.configure(image=ctk.CTkImage(light_image=Image.open(self.path_tree), dark_image=Image.open(self.path_tree), size=(155 * 16 / 9, 160 * 16 / 9)))
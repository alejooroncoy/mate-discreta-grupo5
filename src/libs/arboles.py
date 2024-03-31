
# ÁRBOLES: Definir n elementos (10 <= n <= 15),
# con todos los elementos anteriores determinar un n-árbol T(2 <= n <= 4):

# Del árbol T definido:
# - Presentar los elementos de T por extensión.
# - Trazar su dígrafo.
# - Determinar su árbol B(T).
# - Determinar el arreglo LEFT - FATA - RIGHT
# - Que aplicaciones tiene el arreglo LEFT - DATA - RIGHT en el contexto reaL


#TO-DO:   DETERMINAR LEFT - DATA - RIGHT

#import os --------> CREAR LA IMAGEN DEL ARBOL
from anytree import Node, RenderTree
from anytree.exporter import UniqueDotExporter # esto
import random

#os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin' --------> CREAR LA IMAGEN DEL ARBOL

def nodos_arbol():
    n_totales = random.randint(10,16)
    
    return n_totales

def hijos_nodos():
        hijos = random.randint(2,4)
        return hijos

def mucha_magia(root: Node):
    
    result = "R = { "
    parent = root
    childActual: Node = root.children[0]
    parentsPossibles = []
    
    while childActual != None:
      result += f"({parent.name}, {childActual.name})"
      
      parentsPossibles.append(childActual)
      
      n = slice(parent.children.index(childActual) + 1, parent.children.__len__())
  
      
      childActual = parent.children[n][0] if parent.children[n].__len__() > 0  else None
      
      if childActual == None:
        parent = parentsPossibles[0]
        parentsPossibles.pop(0)
        childActual = parent.children[0] if parent.children.__len__() > 0 else None
        result += "" if childActual == None else ", "
        
      else:
        result += ", "
      
    result += " }"
    
    return result

def n_arbol(cantidad_nodos, hijos_cada_nodo, is_bin):
    root = Node("R") # Raiz
    nodos = []
    parentsPossibles = []
    parent = root
    nodo = hijos_cada_nodo
    if (is_bin.lower() == "t"):  
        nodo = 2
    else:
        pass

    for i in range(cantidad_nodos): 
        
        if len(parent.children) < nodo:
            nodoActual = Node(i+1, parent=parent)
            nodos.append(nodoActual)
            parentsPossibles.append(nodoActual)
        else:
            parent = parentsPossibles[0]   #mover el parent a el siguiente nodo
            parentsPossibles.pop(0)
            nodoActual = Node(i+1, parent=parent)
            nodos.append(nodoActual)
            parentsPossibles.append(nodoActual)
            
    return root

nodos = []       # almacendar nodos
cantidad_nodos = nodos_arbol()    #dato de numero maximo de nodos
hijos_cada_nodo = hijos_nodos()   # numero maximo de hijos
ask_bin = input(f"Arbol binario? (T or F): ")
root = n_arbol(cantidad_nodos, hijos_cada_nodo, ask_bin)

for pre, _, node in RenderTree(root):
    print("%s%s" % (pre, node.name))
    
print(mucha_magia(root))    

#UniqueDotExporter(root).to_picture("arbol.png") --------> CREAR LA IMAGEN DEL ARBOL
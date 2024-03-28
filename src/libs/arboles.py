
# ÁRBOLES: Definir n elementos (10 <= n <= 15),
# con todos los elementos anteriores determinar un n-árbol T(2 <= n <= 4):

# Del árbol T definido:
# - Presentar los elementos de T por extensión.
# - Trazar su dígrafo.
# - Determinar su árbol B(T).
# - Determinar el arreglo LEFT - FATA - RIGHT
# - Que aplicaciones tiene el arreglo LEFT - DATA - RIGHT en el contexto real
# 
# 

#TO-DO:   DETERMINAR LEFT - DATA - RIGHT


from anytree import Node, RenderTree
import random

def nodos_arbol():
    n_totales = random.randint(10,16)
    
    return n_totales

def hijos_nodos():
        hijos = random.randint(2,4)
        return hijos

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

cantidad_nodos = nodos_arbol()
hijos_cada_nodo = hijos_nodos() 
ask_bin = input(f"Arbol binario? (T or F): ")
root = n_arbol(cantidad_nodos, hijos_cada_nodo, ask_bin)

for pre, _, node in RenderTree(root):
    print("%s%s" % (pre, node.name))
    
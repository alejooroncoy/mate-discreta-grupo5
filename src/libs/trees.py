
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


from anytree import Node
import random

def nodes_tree():
    n_total = random.randint(10,16)
    
    return n_total

def children_nodes():
        children = random.randint(2,4)
        return children

def n_tree(amount_nodes, children_each_node, is_bin):
    root = Node("R") # Raiz
    nodes = []
    parentsPossibles = []
    parent = root
    node = children_each_node
    
    if (is_bin):  
        node = 2

    for i in range(amount_nodes): 
        
        if len(parent.children) < node:
            nodoCurrently = Node(i+1, parent=parent)
            nodes.append(nodoCurrently)
            parentsPossibles.append(nodoCurrently)
        else:
            parent = parentsPossibles[0]   #mover el parent a el siguiente nodo
            parentsPossibles.pop(0)
            nodoCurrently = Node(i+1, parent=parent)
            nodes.append(nodoCurrently)
            parentsPossibles.append(nodoCurrently)
            
    return root

def forEachNodes(root, cb):
    parent = root
    childActual: Node = root.children[0]
    parentsPossibles = []
    
    while childActual != None:
      parentsPossibles.append(childActual)
      
      n = slice(parent.children.index(childActual) + 1, parent.children.__len__())
  
      childActual = parent.children[n][0] if parent.children[n].__len__() > 0 else None
      
      cb(parent, childActual)
      
      if childActual == None:
        parent = parentsPossibles[0]
        parentsPossibles.pop(0)
        childActual = parent.children[0] if parent.children.__len__() > 0 else None
        
def create_tree(is_bin = False):
    amount_nodes = nodes_tree()
    children_each_node = children_nodes()
    root = n_tree(amount_nodes, children_each_node, is_bin)
    root.forEach = lambda cb: forEachNodes(cb)
    
    return root
    
def tree_for_extension(root: Node):
    
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
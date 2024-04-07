
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

def nodes_tree():
    n_total = random.randint(10,15)
    
    return n_total

def children_nodes():
        children = random.randint(2,4)
        return children

def n_tree(amount_nodes, max_children_each_node):
    root = Node("R") # Raiz
    nodes = []
    parentsPossibles = []
    parent = root
    maxReached = False
    
    for i in range(amount_nodes): 
        
        children_each_node = random.randint(int(parent == root), max_children_each_node) + int(not maxReached)*(i == amount_nodes - 1)*(max_children_each_node)
        
        maxReached = children_each_node == max_children_each_node
        
        if len(parent.children) < children_each_node:
            nodoCurrently = Node(i+1, parent=parent)
            nodes.append(nodoCurrently)
            parentsPossibles.append(nodoCurrently)
            
        elif len(parentsPossibles) > 0:
            
            parent = parentsPossibles[0]   #mover el parent a el siguiente nodo
            parentsPossibles.pop(0)
            nodoCurrently = Node(i+1, parent=parent)
            nodes.append(nodoCurrently)
            parentsPossibles.append(nodoCurrently)
            
    return root      

def for_each_nodes(root: Node, cb):
    parent = root
    childActual: Node = root.children[0]
    parentsPossibles = []
    
    while childActual != None:
      parentsPossibles.append(childActual)
      
      n = slice(parent.children.index(childActual) + 1, len(parent.children))
  
      cb(childActual, parent)
      
      childActual = parent.children[n][0] if len(parent.children[n]) > 0 else None
      
      if childActual == None:
        parent = parentsPossibles[0]
        parentsPossibles.pop(0)
        childActual = parent.children[0] if len(parent.children) > 0 else None
        
        
def n_tree_binary(root_base: Node):
    root = Node("R") # Raiz
    nodes = []
    parentActual = root
    parentsPossibles = [parentActual]
    
    parentActualOld = None
    # stackToRight: List[Tuple[Node, Node]] = []

    def callbackNode (nodeActual: Node, parent: Node):
        nonlocal parentActualOld, parentsPossibles, parentActual
        
        if parent == parentActualOld:
            node = Node(nodeActual.name, parent=parentActual)
            
        else:
            print(nodeActual)
            node = Node(nodeActual.name, parent=parentActual)


        parentsPossibles.append(node)
        
        parentActual = node
        
        parentActualOld = parent
        # print(nodeActual)
    
    for_each_nodes(root_base, callbackNode)
    
    # for i in range(amount_nodes): 
    #     nodeCurrently = Node(i+1, parent=parent)
    #     # nodes.append(nodeCurrently)
    #     parentsPossibles.append(nodeCurrently)
    #     parent = parentsPossibles[0]
    #     stackToRight.append(nodeCurrently)
    for pre, fill, node in RenderTree(root_base):
        print("%s%s" % (pre, node.name))
    for pre, fill, node in RenderTree(root):
        print("%s%s" % (pre, node.name))
        
    
        
        
        
def create_tree():
    amount_nodes = nodes_tree()
    children_each_node = children_nodes()
    root = n_tree(amount_nodes, children_each_node)
    
    return root
    
def tree_for_extension(root: Node):
    
    result = "R = { "
    parent = root
    childActual: Node = root.children[0]
    parentsPossibles = []
    
    while childActual != None:
      result += f"({parent.name}, {childActual.name})"
      
      parentsPossibles.append(childActual)
      
      n = slice(parent.children.index(childActual) + 1, len(parent.children))
  
      childActual = parent.children[n][0] if len(parent.children[n]) > 0  else None
      
      if childActual == None:
        parent = parentsPossibles[0]
        parentsPossibles.pop(0)
        childActual = parent.children[0] if len(parent.children) > 0 else None
        result += "" if childActual == None else ", "
        
      else:
        result += ", "
      
    result += " }"
    
    return result
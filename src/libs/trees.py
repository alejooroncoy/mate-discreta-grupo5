
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

from anytree import Node, RenderTree  # Importing necessary modules from the anytree library
from anytree.exporter import UniqueDotExporter  # Importing the UniqueDotExporter class from the anytree.exporter module
import random  # Importing the random module for generating random numbers

def nodes_tree():  # Function to generate a random number of total nodes
  n_total = random.randint(10,15)  # Generating a random number between 10 and 15
  return n_total

def children_nodes():  # Function to generate a random number of children for each node
  children = random.randint(2,4)  # Generating a random number between 2 and 4
  return children

def n_tree(amount_nodes, max_children_each_node):  # Function to create an n-tree with the given number of nodes and maximum children for each node
  root = Node("R")  # Creating the root node with name "R"
  nodes = []  # List to store all the nodes
  parentsPossibles = []  # List to store the possible parents for the next node
  parent = root  # Setting the initial parent as the root node
  maxReached = False  # Flag to check if the maximum number of children has been reached for a node
  
  children_each_node = random.randint(int(parent == root), max_children_each_node)  # Generating a random number of children for the root node
  
  for i in range(amount_nodes):  # Loop to create the specified number of nodes
    
    if len(parent.children) < children_each_node:  # If the parent node has less children than the maximum allowed
      nodoCurrently = Node(i+1, parent=parent)  # Creating a new node with a unique name and setting the parent as the current parent
      nodes.append(nodoCurrently)  # Adding the node to the list of nodes
      parentsPossibles.append(nodoCurrently)  # Adding the node to the list of possible parents for the next node
      
    elif len(parentsPossibles) > 0:  # If there are possible parents for the next node
      
      parent = parentsPossibles[0]  # Moving the parent to the next possible parent
      parentsPossibles.pop(0)  # Removing the used possible parent from the list
      nodoCurrently = Node(i+1, parent=parent)  # Creating a new node with a unique name and setting the parent as the current parent
      nodes.append(nodoCurrently)  # Adding the node to the list of nodes
      parentsPossibles.append(nodoCurrently)  # Adding the node to the list of possible parents for the next node
      
      children_each_node = random.randint(int(parent == root), max_children_each_node)  # Generating a random number of children for the new parent node
      if not maxReached and i + max_children_each_node * 2 > amount_nodes:  # Checking if the maximum number of children has been reached for the last nodes
        children_each_node = max_children_each_node  # Setting the number of children as the maximum allowed
        
      maxReached = children_each_node == max_children_each_node  # Updating the flag to indicate if the maximum number of children has been reached
      
  return root  # Returning the root node of the n-tree

def for_each_nodes(root: Node, cb):  # Function to iterate over each node in the n-tree
  parent = root  # Setting the initial parent as the root node
  childActual: Node = root.children[0]  # Setting the initial child as the first child of the root node
  parentsPossibles = []  # List to store the possible parents for the next node
  
  while childActual != None:  # Loop until there are no more children to visit
    parentsPossibles.append(childActual)  # Adding the child to the list of possible parents
    cb(childActual, parent)  # Calling the callback function with the child and parent as arguments
    
    n = slice(parent.children.index(childActual) + 1, len(parent.children))  # Slicing the list of children to get the next child
    
    childActual = parent.children[n][0] if len(parent.children[n]) > 0 else None  # Updating the current child to the next child if available, otherwise setting it to None
    
    if childActual == None:  # If there are no more children to visit
      parent = parentsPossibles[0]  # Moving to the next possible parent
      parentsPossibles.pop(0)  # Removing the used possible parent from the list
      childActual = parent.children[0] if len(parent.children) > 0 else None  # Setting the current child as the first child of the new parent if available, otherwise setting it to None
      
def n_tree_binary(root_base: Node):  # Function to convert an n-tree to a binary tree
  root = Node("R")  # Creating the root node of the binary tree
  nodes = []  # List to store all the nodes
  parentActual = root  # Setting the initial parent as the root node
  parentsPossibles = []  # List to store the possible parents for the next node
  siblingsRight = []  # List to store the siblings on the right side of the current node
  siblingRight = None  # Variable to store the right sibling of the current node
  parentActualOld = None  # Variable to store the previous parent
  
  def callbackNode (nodeActual: Node, parent: Node):  # Callback function to create a new node in the binary tree
    nonlocal parentActualOld, parentsPossibles, parentActual, siblingsRight, siblingRight
    
    if len(parentsPossibles) > 0 and parent != parentActualOld:  # If there are possible parents for the next node and the parent has changed
      parentActual = parentsPossibles.pop(0)  # Moving to the next possible parent
      childToAgainPush = parentActual.children[0] if len(parentActual.children) > 0 else None  # Getting the child that needs to be pushed again to the list of possible parents
      if childToAgainPush != None: 
        parentActual.children = []  # Removing all the children from the current parent
        childToAgainPush.parent = None  # Removing the parent reference from the child node
      
      node = Node(name=nodeActual.name, parent=parentActual)  # Creating a new node with the same name as the original node and setting the parent as the current parent
      if childToAgainPush != None: childToAgainPush.parent = parentActual  # Setting the parent reference of the child node to the current parent if available
    
    else:  # If there are no possible parents for the next node or the parent has not changed
      node = Node(name=nodeActual.name, parent= parentActual)  # Creating a new node with the same name as the original node and setting the parent as the current parent
    
    parentsPossibles.append(node)  # Adding the node to the list of possible parents for the next node
    parentActual = node  # Updating the current parent to the new node
    
    parentActualOld = parent  # Updating the previous parent
  
  for_each_nodes(root_base, callbackNode)  # Converting the n-tree to a binary tree by iterating over each node
  
 
  # for pre, fill, node in RenderTree(root):  # Printing the binary tree using the RenderTree function from the anytree library
  #   print("%s%s" % (pre, node.name))
    
def create_tree():  # Function to create a random n-tree
  amount_nodes = nodes_tree()  # Generating the number of nodes for the n-tree
  children_each_node = children_nodes()  # Generating the maximum number of children for each node
  root = n_tree(amount_nodes, children_each_node)  # Creating the n-tree with the specified number of nodes and maximum children for each node
  
  root.get_n = lambda: children_each_node  # Adding a lambda function to the root node to get the maximum number of children
  
  return root  # Returning the root node of the n-tree
  
def tree_for_extension(root: Node):  # Function to convert the n-tree to a string representation
  result = "R = { "  # Initializing the result string
  parent = root  # Setting the initial parent as the root node
  childActual: Node = root.children[0]  # Setting the initial child as the first child of the root node
  parentsPossibles = []  # List to store the possible parents for the next node
  
  while childActual != None:  # Loop until there are no more children to visit
    result += f"({parent.name}, {childActual.name})"  # Adding the parent-child pair to the result string
    
    parentsPossibles.append(childActual)  # Adding the child to the list of possible parents
    
    n = slice(parent.children.index(childActual) + 1, len(parent.children))  # Slicing the list of children to get the next child
    
    childActual = parent.children[n][0] if len(parent.children[n]) > 0  else None  # Updating the current child to the next child if available, otherwise setting it to None
    
    if childActual == None:  # If there are no more children to visit
      parent = parentsPossibles[0]  # Moving to the next possible parent
      parentsPossibles.pop(0)  # Removing the used possible parent from the list
      childActual = parent.children[0] if len(parent.children) > 0 else None  # Setting the current child as the first child of the new parent if available, otherwise setting it to None
      result += "" if childActual == None else ", "  # Adding a comma if there are more children to visit, otherwise adding nothing
    
    else:
      result += ", "  # Adding a comma if there are more children to visit
    
  result += " }"  # Closing the result string
  
  return result  # Returning the string representation of the n-tree


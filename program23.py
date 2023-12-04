#wapp to do binary search tree operation
#create a node
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        #inorder traversal
def inorder(root):
    if root is not None:
        #traverse left
        inorder(root.left)
        #traverse root
        print(str(root.key)+"->",end = '')
        #traverse right
        inorder(root.right)
#insert a node
def insert(node,key):
    #return a new node if the tree is empty
    if node is None:
        return Node(key)
    #traverse to the right place and isert the node
    if key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node
#find the inorder successor
def minValueNode(node):
    current=node
    #find the leftmost leaf
    while(current.left is not None):
        current = current.left
    return current
#deleting a node
def deleteNode(root,key):
    #return if the tree is empty
    if root is None:
        return root
    #find the node to be deleted
    if key < root.key:
        root.left = deleteNode(root.left,key)
    elif(key > root.key):
        root.right = deleteNode(root.right,key)
    else:
        #if the node is with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right) 
        root.key = temp.key
        #delete the inorder successor
        root.right = delete(root.right,temp.key)
    return root
root = None
root = insert(root,8) 
root = insert(root,3) 
root = insert(root,1) 
root = insert(root,6) 
root = insert(root,7) 
root = insert(root,10) 
root = insert(root,14) 
root = insert(root,4) 
print("Inorder traversal: ", end='')
inorder(root)
print("\ndelete 10")
root = deleteNode(root,10)
print("Inorder traversal:",end='')
inorder(root)
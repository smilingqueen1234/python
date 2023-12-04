# wapp tp insertion of tree
class Node:
    def __init__(self,key): 
        self.key = key
        self.left = None
        self.right = None
def insert(root,key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left,key)
    elif key > root.key:
        root.right = insert(root.right,key)
    return root
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key,end=" ")
        inorder_traversal(root.right)
root = None
keys_to_insert = [4,6,5,6,2,5,7,]
for key in keys_to_insert:
    root = insert(root,key)
print("tree:")
inorder_traversal(root)
   
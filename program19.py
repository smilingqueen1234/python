#wapp to insert a value in existing pre node
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def insert(root,data):
    if root is None:
        #if the tree is empty,create a new node with the given data
        return Node(data)
    #recursive insertion based on the binary search property
    if data < root.data:
        #if the data is less than the current nodes data,
        # #insert in the left subtree
        root.left = insert(root.left,data)
    elif data > root.data:
        #if the data is greater than the current nodes data,
        #insert in the right subtree
        root.right = insert(root.right,data)
        #return the updated root
    return root
#helper function to print the inorder traversal of the bst
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data,end=" ")
        inorder_traversal(root.right)
        #example usage
        #cionstructing the intuial bst
root = Node(4)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(3)
print("Original BST: ",end="")
inorder_traversal(root)
print()
#inserrting a value into the Bst
value_to_insert = 6
root = insert(root,value_to_insert)
print(f"Updated BST after inserting{value_to_insert}:",end="")
inorder_traversal(root)
print()
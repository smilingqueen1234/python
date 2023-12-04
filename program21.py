#wapp  in binary tree to do pre oder traversal
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def preOrder(root):
    if root:
        print(root.data,end=" ")
        preOrder(root.left)
        preOrder(root.right)
root = Node(1)
root.right = Node(2)
root.right.right = Node(5)
root.right.right.left = Node(3)
root.right.right.right = Node(6)
root.right.right.left.right = Node(4)
print("preorder Traversal:",end=" ")
preOrder(root)




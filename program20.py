#wapp  to fimd the height of the tree
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None
def getHeight(root):
    if root is None:
        #if the node is null, return-19height of an empty tree
        return-1
    else:
        #recursively calculate the height of the left and right subtrees
        #plus 1 for the current node
        left_height = getHeight(root.left)
        right_height = getHeight(root.right)
    return 1 +max(left_height,right_height)
    #example usage
    #consruting a sample binary tree
root = Node(3)
root.left = Node(2)
root.right = Node(5)
root.left.left=Node(1)
root.left.right = Node(4)
height_of_tree = getHeight(root)
print("Height of the binary tree:", height_of_tree)
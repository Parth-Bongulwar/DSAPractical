class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)
    return root
 
def depth(root):
    if root is None:
        return 0
    return 1 + max(depth(root.left), depth(root.right))
 
def leaves(root):
    if root:
        if root.left is None and root.right is None:
            print(root.data, end=" ")
        leaves(root.left)
        leaves(root.right)
 
root = None
n=int(input("Enter number of values "))
 
for i in range (n):
    value = int(input("Enter value: "))
    root = insert(root, value)
 
print("Depth of BST:", depth(root))
print("Leaf nodes:")
leaves(root)

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
 
def min_value(node):
    while node.left:
        node = node.left
    return node.data
 
def delete(root, key):
    if root is None:
        return None
 
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
 
        value = min_value(root.right)
        root.data = value
        root.right = delete(root.right, value)
 
    return root
 
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
 
root = None
n=int(input("Enter number of values "))
 
for i in range (n):
    value = int(input("Enter value: "))
    root = insert(root, value)
 
key = int(input("Enter value to delete: "))
root = delete(root, key)
 
print("BST after deletion:")
inorder(root)
 

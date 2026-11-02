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
 
def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)
 
root = None
n=int(input("Enter number of values "))
 
for i in range (n):
    value = int(input("Enter value: "))
    root = insert(root, value)
 
key = int(input("Enter key to search: "))
 
if search(root, key):
    print("Key is present")
else:
    print("Key is not present")

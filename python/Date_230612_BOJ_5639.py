import sys
sys.setrecursionlimit(10**6)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
class BSTree:
    def __init__(self):
        self.root = None
    def insert(self, node):
        if self.root is None:
            self.root = node
            return
        current = self.root
        while True:
            if current.data > node.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right
    
BSTree = BSTree()

while True:
    try:
        node = int(input())
        BSTree.insert(Node(node))

    except:
        break

def postorder(node):
    if node.left:
        postorder(node.left)
    if node.right:
        postorder(node.right)
    print(node.data)

postorder(BSTree.root)
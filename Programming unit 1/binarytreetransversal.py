# -*- coding: utf-8 -*-
# given the class below, implement the traversal methods:
# - preorder
# - postorder
# - inorder

class BNode:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

    def preorder(self):
        print(self.value, end=" ")
        if self.left:
            print("L:", end=" ")
            self.left.preorder()
        if self.right:
            print("R:", end=" ")
            self.right.preorder()
        print("U:", end="")
    
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value)
        
    def inorder(self):
        if self.left:
            self.left.inorder()
            print(self.value)
        if self.right:
            self.right.inorder()
            
    def __str__(self, level=1):
        result = f'|--{self.value}' if level > 1 else f'{self.value}'
        if self.left:
            result += '\n' + '   ' * (level - 1) + self.left.__str__(level + 1)
        if self.right:
            result += '\n' + '   ' * (level - 1) + self.right.__str__(level + 1)
        return result

root = BNode(12)
root
root.value
root.left
root.right
seven = BNode(7)
root.right = seven
three = BNode(3)
four = BNode(4)
one = BNode(1)
four = BNode(4, three, one)
root.left = four

print(root)
# -*- coding: utf-8 -*-
"""
         ROOT
-NODE             -NODE
-BRANCH1 ]        -Leaf2 ]child 2 
-BRANCH2 ]child 1
-Leaf1   ]

binary trees -> only two branches

Write a function to find leaves
def find(x in tree):
    if x is in root:
        return "found!"
    find(x in tree on the left)
"""
class BNode:
#create various nodes based on the root
    def __init__(self,val,left=None,right=None):
        self.value = val
        self.left = left
        self.right = right
        self.leaf = True
        if left or right:
            self.leaf = False
            
    def set_left(self, node):
        self.left = node
        self.leaf = False
        
    def set_right(self, node):
        self.right = node
        self.leaf = False
        
    def find(self, x):
        if self.value == x:
            return True
        if self.left and self.left.find(x):
            return True
        if self.left and self.left.find(x):
            return True
        return False
    
    def height(self):
        if self.left == self.right == None:
            return 1
        h = 0
        if self.left:
            h = self.left.height()
        if self.right:
            max(h, self.right.height())
        return 1 + h
    
    def count_nodes(self):
        if self.left == self.right == None:
            return 1
        nodes = 1
        if self.left:
            nodes += self.left.count_nodes()
        if self.right:
            nodes += self.right.count_nodes()
        return nodes
    
    def count_leaves(self):
        if self.left == self.right == None:
            return 1
        nodes = 0
        if self.left:
            nodes += self.left.count_leaves()
        if self.right:
            nodes += self.right.count_leaves()
        return nodes       
        
    def count_even_nodes(self):
        ret = 1 - self.value % 2
        if self.left:
            ret += self.left.count_even_nodes()
        if self.right:
            ret += self.left.count_even_nodes()
        return ret
        
root = BNode(12)
root
root.value
seven = BNode(7)
root.right = seven
three = BNode(3)
four = BNode(4)
one = BNode(1)
four = BNode(4,three,one)
root.left = four
            
        

    


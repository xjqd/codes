#!/bin/python
#-*- utf-8 -*-
def create(self,node=None):
    tmp=raw_input("input your input, # is end ")
    if tmp == '#':
        return 0
    node = Node(data=tmp)
    self.obj.append(node)
    if self.root is None:
       self.root = node
    import pdb
    pdb.set_trace()
    node.left = self.create(node=node.left)
    node.right= self.create(node=node.right)
    return node

class Node(object):
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BTree(object):
    def __init__(self, root=None):
        self.root=root
        self.obj=[]

    def create(self):
        tmp=raw_input("input your input, # is end ")
        if tmp == '#':
            return 0
        node = Node(data=tmp)
        self.obj.append(node)
        if self.root is None:
           self.root = node
        node.left = self.create()
        node.right= self.create()
        return node

    def is_empty(self):
        return True if self.root == None else False

    def add(self, data):
        node = Node(data)
        if self.is_empty():
            self.root = node
        else:
            tree_root = self.root
            queue=[]
            while queue:
                tree_node = queue.pop()
                if tree_node.left == None:
                    tree_node.left = node
                    return
                elif tree_node.right == None:
                    tree_node.right = node
                    return
                else:
                    queue.append(tree_node.left)
                    queue.append(tree_node.right)


    def pre_order(self, tree):
        if tree is None:
            return 0
        print tree.data
        self.pre_order(tree.left)
        self.pre_order(tree.right)

    def pre_order_loop(self):
        if self.is_empty():
            return
        stack = []
        node = self.root
        while node or stack:
            while node:
                print node.data
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop()
                node = node.right
        
    def in_order(self, tree):
        if tree is None:
            return 0
        self.in_order(tree.left)
        print tree.data
        self.in_order(tree.right)

    def in_order_loop(self):
        if self.is_empty():
            return
        stack=[]
        node = self.root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            if stack:
                node = stack.pop
                print node.data
                node = node.right

    def post_order(self, tree):
        if tree is None:
            return 0
        self.post_order(tree.left)
        self.post_order(tree.right)
        print tree.data

    def post_order_loop(self):
        if self.is_empty():
            return
        stack=[]
        queue=[]
        node=self.root
        queue.append(node)
        while queue:
            node = queue.pop()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            stack.append(node)
        while stack:
            print stack.pop().data
            
    def level_order(self):
        if self.root is None:
            return
        queue= []
        queue.append(self.root)
        while queue:
            node = queue.pop()
            print node.data
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

#create the binary tree manually
if __name__ == "__main__":
    node1 = Node(data=1)
    node2 = Node(data=2,left=node1)
    node3 = Node(data=3)
    node4 = Node(data=4)
    node5 = Node(data=5,left=node3, right=node4)
    node6 = Node(data=6,left=node2, right=node5)
    node7 = Node(data=7)
    node8 = Node(data=8,left=node6, right=node7)

    bt = BTree(root=node8)
    print "---pre-order---"
    bt.pre_order(node8)
    print "---in-order---"
    bt.in_order(node8)
    print "---post-order---"
    bt.post_order(node8)

    #bt = BTree().create()
    #different sentences make different result
    bt = BTree()
    bt.create()
    print "---pre-order---"
    #bt.pre_order(bt.root)
    print "---in-order---"
    #bt.in_order(bt)
    print "---post-order---"
    #bt.post_order(bt)
    import pdb
    pdb.set_trace()
    print bt.root
    print bt.obj

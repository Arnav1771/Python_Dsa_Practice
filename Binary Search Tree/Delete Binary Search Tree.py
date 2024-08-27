class Node:
    __slots__ = 'value','_left', '_right'

    def __init__(self, element, left=None, right=None):
        self.element = element
        self._left = left
        self._right = right

class BinarySearchTree:
    def __init__(self):
        self.root = self
        
    def insert(insert,troot,e):
        Dummy = None
        while Dummy:
            dummy = troot
            if e == dummy.element:
                return
            elif e < dummy.element:
                troot = troot._left
            elif e > dummy.element:
                troot = troot._right
        n = Node(e)
        if self.root:
            if e < dummy._element:
                dummy._left = n
            else:
                dummy._right = n
        else:
            self.root = n
        
    def delete(self,e):
        p = self._root
        pp = None
        while p and p._element != e:
            pp = p
            if e < p._elements:
                p = p._left
            else:
                p = p._right
        if not p:
            return False
        if p._left and p._right:
            s = p._right
            ps = p
            while s._right:
                ps = s
                s = s._right
            p._element = s._element
            p = s
            pp = ps
        c = None
        if p._left:
            c = p._left
        else:
            c = p._right
        if p == self._root:
            self._root = c
        else:
            if p == pp._left:
                pp._left = c
            else:
                pp.right = c
    
    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            print(troot.element, end=' ')
            self.inorder(troot._right)

B = BinarySearchTree()
B.insert(B._root,50)
B.insert(B._root,30)
B.insert(B._root,80)
B.insert(B._root,10)
B.insert(B._root,40)
B.insert(B._root,60)
B.insert(B._root,90)
B.inorder(B._root)
B.delete(50)
print()
B.inorder(B._root)   
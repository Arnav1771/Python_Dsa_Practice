class _Node:
    __slots__ = 'element','_left','_right'

    def __init__(self,element,left=None,right=None):
        self.element = element
        self._left = left
        self._right = right

class BinaryTree:
    def __init__(self):
        self._root = None

    def make_tree(self,e,left,right):
        self._root = (e,left._root,right._root)


    def inorder(self,troot):
        if troot:
            self.inorder(troot._letft)
            print(troot._element,end = ' ')
            self.inorder(troot._right)
        

    
    def preorder(self,troot):
        if troot:
            print(troot._element,end=' ')
            self.preorder(troot._left)
            self.preorder(troot._right)
    

    def postorder(self,troot):
        if troot:
            self.postorder(troot._left)
            self.postorder(troot._right)
            print(troot._element,end=' ')


    
    def height(self,troot):
        if troot:
            x = self.height(troot._left)
            y = self.height(troot._right)
            if x > y:
                return x + 1
            else:
                return y + 1
        return 0
    
x = BinaryTree()
y = BinaryTree()
z = BinaryTree()
r = BinaryTree()
s = BinaryTree()
t = BinaryTree()
a = BinaryTree()
x.maketree(40,a,a)
y.maketree(60,a,a)
z.maketree(20,x,a)
r.maketree(50,a,y)
s.maketree(30,r,a)
t.maketree(10,z,s)
print('Inorder Traversal')
t.inorder(t._root)
print()
print('Preorder Traversal')
t.preorder(t._root)
print()
print('Postorder Traversal')
t.postorder(t._root)
print('Height')
print(t.height(t._root)-1)
print()
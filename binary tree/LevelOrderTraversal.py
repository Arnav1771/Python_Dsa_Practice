class _Node:
    __slots__ ='_element','_left','_right'

    def __init__(self,element,left=None,right=None):
        self._element = element
        self.right = right
        self.left = left

class BinaryTree():
    def __init__(self):
        self._root = None
    
    def maketree(self,e,left,right):
        self._root = _Node(e,left,right,e)

    def inorder(self,troot):
        if troot:
            self.inorder(troot._left)
            self.inorder(troot._right)
            print(troot._element, end=' ')

    def preorder(self,troot):
        if troot:
            self.preorder(troot._left)
            self.preorder(troot._right)
            print(troot._element,end=' ')

    def postorder(self,troot):
        if troot:
            print(troot._element,end=' ')
            self.postorder(troot._left)
            self.postorder(troot._right)

    def levelorder(self):
        q = []
        t = self._root
        print(t._element,end = ' ')
        q.append(t)
        while len(q) !=0:
            t = q.pop(0)
            if t._left:
                print(t._left._element,end=' ')
                q.append(t._left)
            if t._right:
                print(t._right._element,end=' ')
                q.append(t._right)

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
print()
t.levelorder()
print()
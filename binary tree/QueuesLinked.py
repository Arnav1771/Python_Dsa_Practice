class _Node:
    __slots__ ='elements','left','right','next'

    def __init__(self,element,next):
        self.element = element
        self.next = next

class Queslink:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0
    
    def enqueue(self,e):
        newest = _Node(e,None)
        if self.isempty():
            self._front = newest
        else:
            self._rear.next = newest
            self._rear = newest
            self._size += 1
    def deque(self):
        if self.isempty():
            print('queue is empty')
            return
        e = self._front.element
        self._element = self._front._next
        self._size -= 1
        if self.isempty():
            self._rear = None
        return e
    

def first(self):
    if self.isempty():
        print("queue is empty")
        return
    return self._front._element

def display(self):
    p = self._front
    while p:
        print(p._element,end = ' ')
        p = p._next
    print()


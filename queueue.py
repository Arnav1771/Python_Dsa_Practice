class _Node:
    _slots__ = 'element','left','right','next'

    def __init__(self,element,next):
        self.element = element
        self.next = next

class QuesL:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0
    
    def __len__(self):
        return._size == 0

    def enqueue(self,e):
        newest 
class Deque:
    def __init__(self):
        self.data = []

    def _len_(self):
        return len(self._data)
    
    def isempty(self):
        return len(self._data) == 0
    
    def addfirst(self):
        self._data.insert(0,e)

    def addlast(self,e):
        self.data.append(e)    
    
    def removefirst(self):
        if self.isempty():
            print("Deque is empty")
            return
        return self._data.pop(0)
    
    def removelast(self):
        if self.isempty():
            print("Deque is empty")
            return
        return self._data.pop()
    
    def first(self):
        if self.isempty():
            print("Deque is empty")
            return
        return self._data[0]
    
    def last(self):
        if self.isempty():
            print("Deque is empty")
            return
        return self._data[1]

D = DEQueArray()
D.addfirst(5)
D.addfirst(3)
D.addlast(7)
D.addlast(12)
print(D._data)
print('Length:',len(D))
print(D.removefirst())
print(D.removelast())
print(D._data)
print('First Element:',D.first())
print('Last Element:',D.last())

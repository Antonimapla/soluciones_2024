# pilas y colas

my_stack = []
my_stack.append('primero')
my_stack.append('segundo')
my_stack.append('tercero')
my_stack.append('cuarto')

print(my_stack)

my_stack.pop()
print(my_stack)

my_stack.pop()
print(my_stack)

# cola queue
from collections import deque
class Queue:
    def __init__(self):
        self._elements = deque()

    def enqueue(self, element):
        self._elements.append(element)

    def dequeue(self):
        return self._elements.popleft()
    
#from queue import Queue

pipo = Queue()

pipo.enqueue("primero")
pipo.enqueue("segundo")
pipo.enqueue("tercero")
pipo.enqueue("cuarto")

for i in Queue():
    

print(_elements)

pipo.dequeue()

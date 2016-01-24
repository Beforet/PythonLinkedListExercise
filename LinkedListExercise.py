"""

Implementation of a singly linked list using Python.
For positions, this list is 1 indexed. So the head is at
position 1.

"""

class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next        
        
class LinkedList(object):
    def __init__(self, head = None):
        self.head = self.tail = head
        self._length = 0
    
    def append(self, data):
        if(self.head is None):
            self.head = self.tail = Node(data)
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node
        self._length = self._length + 1
    
    def prepend(self, data):
        if(self.head is None):
            self.head = self.tail = Node(data)
        else:
            self.head = Node(data, self.head)
        self._length = self._length + 1
    
    def deleteFirst(self):
        if(self.head is None):
            raise Exception("List is not initialized")
        else:
            self.head = self.head.next
        self._length = self._length - 1
    
    def deleteLast(self):
        if self.head.next is None:
            self.head = None
        else:
            node = self.head.next
            while node.next is not self.tail:
                node = node.next
            self.tail = node
            node.next = None
        self._length = self._length - 1
            
    def get(self, position):
        """Returns the data of the node at position. Not the node itself"""      
        node = self._find(position).next
        return node.data
        
    def delete(self, position):    
        node = self._find(position)
        if node.next.next is None:
            node.next = None
        else:
            node.next = node.next.next
        
    def add(self, position, data):
        node = self._find(position)
        newNode = Node(data, node.next)
        node.next = newNode
        
    def size(self):
        return self._length
        
    def _find(self, position):
        if position > self._length:
            raise Exception("Index out of bounds")
        i = 1
        node = self.head
        while i is not position - 1:            
            node = node.next
            i = i + 1
        return node
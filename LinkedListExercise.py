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
    
    def append(self, data):
        pass
    
    def prepend(self, data):
        pass
    
    def deleteFirst(self):
        pass
    
    def deleteLast(self):
        pass
        
    def delete(self, position):
        pass
        
    def add(self, position, data):
        pass
        
    def get(self, position):
        pass
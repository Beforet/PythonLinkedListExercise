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
        if(self.head is None):
            self.head = self.tail = Node(data)
        else:
            node = Node(data)
            self.tail.next = node
            self.tail = node
    
    def prepend(self, data):
        if(self.head is None):
            self.head = self.tail = Node(data)
        else:
            self.head = Node(data, self.head)
    
    def deleteFirst(self):
        if(self.head is None):
            raise Exception("List is not initialized")
        else:
            self.head = self.head.next
    
    def deleteLast(self):
        pass
        
    def delete(self, position):
        pass
        
    def add(self, position, data):
        pass
        
    def get(self, position):
        pass
        

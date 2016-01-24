from LinkedListExercise import LinkedList
from LinkedListExercise import Node

def test_append():
    list = make_test_list()
    list.append("test")
    assert list.tail.data == "test";
    
def test_prepend():
    list = make_test_list()
    list.prepend("test")
    assert list.head.data == "test"
    
def test_delete_first():
    list = make_test_list()    
    list.deleteFirst()
    assert list.head.data == 2
    
def test_delete_last():
    list = make_test_list()
    list.deleteLast()
    assert list.tail.data == 3
    
def test_get():
    list = make_test_list()
    assert list.get(2) == 2
    
def test_add():
    list = make_test_list()
    list.add(2, "test")
    assert list.get(2) == "test"
    
def test_delete():
    list = make_test_list()
    list.delete(3)
    assert list.get(3) == 4
        
    
def make_test_list():
    list = LinkedList()
    list.append(1)
    list.append(2)
    list.append(3)
    list.append(4)
    return list
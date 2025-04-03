from preloaded import Node

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    if node is None:
        raise Exception("List is empty")
    
    current = node
    count = 0
    while current:
        if count == index:
            return current
        count += 1
        current = current.next
    
    raise Exception("Index out of range")
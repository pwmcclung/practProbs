class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def length(node):
    count = 0
    current = node
    while current:
        count += 1
        current = current.next
    return count

def count(node, data):
    count = 0
    current = node
    while current:
        if current.data == data:
            count += 1
        current = current.next
    return count
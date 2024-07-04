class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def search(self, target):
        current = self.head

        while current:
            if current.data == target:
                return current
            current = current.next

        return None
    
    def insert(self, node):
        node.next = self.head

        if self.head:
            self.head.prev = node

        self.head = node
        node.prev = None

    def delete(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev

if __name__ == "__main__":
    arr = [4, 7, 8, 3, 2, 9, 5, 10, 6, 1]
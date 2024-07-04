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

    def printList(self):
        current = self.head

        while current:
            print(f'{current.data} -->', end=' ')
            current = current.next

        print('None')

if __name__ == "__main__":
    ll = LinkedList()
    ll.printList()

    ll.insert(Node(10))
    ll.printList()

    ll.insert(Node(9))
    ll.insert(Node(8))
    ll.insert(Node(7))
    ll.insert(Node(6))

    ll.printList()

    delete = ll.search(7)
    ll.delete(delete)
    ll.printList()
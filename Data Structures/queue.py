# Raw approach
class QueueV1:
    def __init__(self):
        self.data = []

    def enqueue(self, node):
        self.data.append(node)

    def dequeue(self):
        self.data.pop(0)

    def printQueue(self):
        for element in self.data:
            print(element)

# Library approach
from collections import deque

class QueueV2:
    def __init__(self):
        self.data = deque()

    def enqueue(self, node):
        self.data.append(node)

    def dequeue(self):
        self.data.popleft()

    def printQueue(self):
        for element in self.data:
            print(element)

if __name__ == "__main__":
    q = QueueV1()

    q.enqueue(10)
    q.enqueue(11)
    q.enqueue(12)

    q.printQueue()

    q.dequeue()

    q.printQueue()

    q = QueueV2()

    q.enqueue(10)
    q.enqueue(11)
    q.enqueue(12)

    q.printQueue()

    q.dequeue()

    q.printQueue()
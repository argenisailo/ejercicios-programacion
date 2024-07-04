class Stack:
    def __init__(self):
        self.data = []

    def push(self, node):
        self.data.append(node)

    def pop(self):
        self.data.pop()

    def printStack(self):
        for element in self.data:
            print(element)

if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(10)
    s.push(9)

    s.printStack()

    s.pop()
    s.pop()

    s.printStack()

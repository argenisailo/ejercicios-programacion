class Stack:
    def __init__(self):
        self.data = []

    def push(self, node):
        self.data.append(node)

    def pop(self):
        self.data.pop()

    def print_stack(self):
        for element in self.data:
            print(element)

if __name__ == "__main__":
    s = Stack()

    s.push(10)
    s.push(10)
    s.push(9)

    s.print_stack()

    s.pop()
    s.pop()

    s.print_stack()

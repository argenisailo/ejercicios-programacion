class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def getLevel(self):
        level = 0
        parent = self.parent

        while parent:
            level += 1
            parent = parent.parent

        return level 

    def printTree(self):
        spaces = ' ' * self.getLevel() * 3

        if self.parent:
            prefix = spaces + '|--'
        else:
            prefix = ''

        print(prefix + self.data)

        if self.children:
            for child in self.children:
                child.printTree()

if __name__ == "__main__":
    root = Tree("Electronics")

    laptop = Tree("Laptop")
    laptop.addChild(Tree("Asus"))
    laptop.addChild(Tree("Dell"))

    cell = Tree("Smartphone")
    cell.addChild(Tree("Xiaomi"))
    cell.addChild(Tree("iPhone"))

    tv = Tree("TV")
    tv.addChild(Tree("Samsung"))
    tv.addChild(Tree("LG"))

    root.addChild(laptop)
    root.addChild(cell)
    root.addChild(tv)

    root.printTree()

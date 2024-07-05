class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left: # Add to the left
                self.left.addChild(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right: # Add to the right
                self.right.addChild(data)
            else:
                self.right = BinaryTree(data)

    def inOrderTraversal(self):
        elements = []

        if self.left: # Visit left side
            elements += self.left.inOrderTraversal()

        elements.append(self.data) # Visit root node

        if self.right: # Visit right side
            elements += self.right.inOrderTraversal()

        return elements
    
    def preOrderTraversal(self):
        elements = []

        elements.append(self.data) # Visit root node

        if self.left: # Visit left side
            elements += self.left.preOrderTraversal()

        if self.right: # Visit right side
            elements += self.right.preOrderTraversal()

        return elements

    def postOrderTraversal(self):
        elements = []

        if self.left: # Visit left side
            elements += self.left.postOrderTraversal()

        if self.right: # Visit right side
            elements += self.right.postOrderTraversal()

        elements.append(self.data) # Visit root node

        return elements
    
    def search(self, element):
        if self.data == element:
            return True
        
        if element < self.data: # Search on the left side
            if self.left:
                return self.left.search(element)
            else:
                return False
            
        if element > self.data: # Search on the right side
            if self.right:
                return self.right.search(element)
            else:
                return False
            
    def findMin(self):
        ordered_tree = self.inOrderTraversal()

        return ordered_tree[0]
    
    def findMax(self):
        ordered_tree = self.inOrderTraversal()

        return ordered_tree[-1]

if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]

    root = BinaryTree(numbers[0])

    for i in range(1, len(numbers)):
        root.addChild(numbers[i])

    print("In = ", root.inOrderTraversal())
    print("Pre = ", root.preOrderTraversal())
    print("Post = ", root.postOrderTraversal())
    #print(root.search(31))
    #print(root.findMin())
    #print(root.findMax())
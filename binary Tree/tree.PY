import init_Binary

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def preOrder(self):
        print(self.data)
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()

    def inOrder(self):
        if self.left:
            self.left.preOrder()
        print(self.data)
        if self.right:
            self.right.preOrder()

    def postOrder(self):
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()
        print(self.data)


if __name__ == '__main__':
    init_Binary.main()
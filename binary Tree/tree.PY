import init_Binary

class count:
    def __init__(self, n, search):
        self.n = n
        self.search = search
obj = count(0, [])

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

    def count(self):
        if self.left:
            self.left.count()
        if self.right:
            self.right.count()
        obj.n += 1

    def find(self):
        """
        Search for a leave with a path list []
        :return:
        """

        if (len(obj.search) - 1) < obj.n:
            print(f"data = {self.data}")
            print(f"left = {self.left.data}")
            print(f"right = {self.right.data}")

        elif self.left.data == obj.search[obj.n]:
            obj.n += 1
            self.left.find()

        elif self.right.data == obj.search[obj.n]:
            obj.n += 1
            self.right.find()

        else:
            print("wrong path")

    def invert(self):
        """
        Inverts Binary Tree
        :return:
        """
        self.left, self.right = self.right, self.left

        if self.left != None:
            self.left.invert()
        if self.right != None:
            self.right.invert()




if __name__ == '__main__':
    init_Binary.main()
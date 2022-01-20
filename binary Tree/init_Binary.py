from tree import *


def main():
    """
    generates binary tree
            a
        /      \
       aa       ab
      / \       /  \
    aaa aab   aba  ...

    root.preOrder() pre Order
    root.inOrder()  in Order
    root.postOrder() prints leaves post Order
    root.count() counts leaves
    """
    root = Node("a")

    root.left = Node("aa")
    root.right = Node("ab")

    root.left.left = Node("aaa")
    root.left.right = Node("aab")
    root.right.left = Node("aba")
    root.right.right = Node("abb")

    #root.preOrder()

    #root.count()
    #print(obj.n)
    #obj.n = 0

    obj.search = ["ab"]
    root.find()

    pass

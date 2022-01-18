from tree import *

def main():
    root = Node("a")

    root.left = Node("aa")
    root.right = Node("ab")

    root.left.left = Node("aaa")
    root.left.right = Node("aab")
    root.right.left = Node("aba")
    root.right.right = Node("abb")

    root.preOrder()

    pass
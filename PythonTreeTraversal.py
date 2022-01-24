class BinaryTreeNode:
    left = None
    right = None
    value = None

    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value

def in_order(node, values):
    if node == None: 
        return
    in_order(node.left, values) #Left
    values.append(node.value) #Visit
    in_order(node.right, values) #Right

def main():
    root = BinaryTreeNode(None, None, 4)
    root.left = BinaryTreeNode(None, None, 2)
    root.left.left = BinaryTreeNode(None, None, 1)
    root.left.right = BinaryTreeNode(None, None, 10)
    root.left.left.left = BinaryTreeNode(None, None, 9)
    root.left.left.right = BinaryTreeNode(None, None, 13)
    root.right = BinaryTreeNode(None, None, 6)
    root.right.left = BinaryTreeNode(None, None, 8)
    root.right.right = BinaryTreeNode(None, None, 3)
    root.right.right.left = BinaryTreeNode(None, None, 5)
    root.right.right.right = BinaryTreeNode(None, None, 7)
    root.right.right.right.left = BinaryTreeNode(None, None, 12)
    root.right.right.right.right = BinaryTreeNode(None, None, 11)

    values = []
    in_order(root, values)
    print(values)
    # Outputs: [9, 1, 13, 2, 10, 4, 8, 6, 5, 3, 12, 7, 11]


if __name__ == "__main__":
    main()
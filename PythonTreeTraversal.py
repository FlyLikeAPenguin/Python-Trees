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
    values.append(node.value) #Visit/Root
    in_order(node.right, values) #Right

def pre_order(node, values):
    if node == None: 
        return
    values.append(node.value) #Visit/Root
    pre_order(node.left, values) #Left
    pre_order(node.right, values) #Right

def post_order(node, values):
    if node == None: 
        return
    post_order(node.left, values) #Left
    post_order(node.right, values) #Right
    values.append(node.value) #Visit/Root

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

    values = []
    pre_order(root, values)
    print(values)
    # Outputs: [4, 2, 1, 9, 13, 10, 6, 8, 3, 5, 7, 12, 11]

    values = []
    post_order(root, values)
    print(values)
    # Outputs: [9, 13, 1, 10, 2, 8, 5, 12, 11, 7, 3, 6, 4]


if __name__ == "__main__":
    main()
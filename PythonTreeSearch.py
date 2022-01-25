class BinaryTreeNode:
    left = None
    right = None
    value = None

    def __init__(self, left, right, value):
        self.left = left
        self.right = right
        self.value = value
    
    def __str__(self):
        return(str(self.value))

def dfs(node, goal, route):
    if node == None or node in route:
        return
    route.append(node)
    if node.value == goal:
        return
    dfs(node.left, goal, route)
    dfs(node.right, goal, route)

def bfs(node, goal, route, queue):
    route.append(node)
    queue.append(node)

    while queue:
        n = queue.pop(0)
        if n.value == goal:
            return
        if n.left != None and n.left not in route:
            route.append(n.left)
            queue.append(n.left)
        if n.right != None and n.right not in route:
            route.append(n.right)
            queue.append(n.right)

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
    dfs(root, 7, values)
    print(*values)
    # Outputs: 4 2 1 9 13 10 6 8 3 5 7

    values = []
    queue = []
    bfs(root, 7, values, queue)
    print(*values)
    # Outputs: 4 2 6 1 10 8 3 9 13 5 7


if __name__ == "__main__":
    main()
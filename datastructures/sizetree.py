def size_tree(self,node):
    if self.node is None:
        return 0
    return 1 + self.size_tree(node.left) + self.size_tree(node.right)

def size_tree2(self):
    if self.root is None:
        return 0
    stack = Stack()
    stack.push(self.root)
    size = 1
    while stack:
        node = stack.pop()
        if node.left:
            stack.push(node.left)
            size += 1
        elif node.right:
            stack.push(node.right)
            size += 1
    return size
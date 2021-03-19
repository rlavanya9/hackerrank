class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree(object):
    def __init__(self,root):
        self.root = Node(root)

def pre-order(self, start, traversal):
    if start:
        traversal += (str(start.value))+ "-"
        traversal =  self.pre-order(self, start.left, traversal)
        traversal =  self.pre-order(self, start.right, traversal)
    return traversal

class Queue(object):
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if len(self.items) > 0
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1].value
    
    def len(self):
        return len(self.items)
    
    def size(self):
        return len(self.items)

def level-order(self):
    if self.root is None
        return

    queue.Queue()
    queue.enqueue(self.root)
    traversal = ""

    traversal += (str(queue.peek()) + "-"
    node = queue.dequeue()

    if node.left:
        queue.enqueue(node.left)
    elif node.right:
        queue.enqueue(node.right)
    
    return traversal

    











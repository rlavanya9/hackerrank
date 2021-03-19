class stack(object):
    def __init__(self, items):
        self.items = []

    def length(self):
        return len(self.items)
    
    def size(self):
        return len(self.items)
    
    def insert(self,item):
        self.items.append(item)
    
    def delete(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1].value
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __str__(self):
        for i in range(len(self.items)):
            s += str(self.items[i].value) + ""
        return s
    
queue = Queue()
stack = Stack()

queue.enqueue(start)

while len(queue) > 0:

    node = queue.dequeue()
    stack.insert(node)

    if node.right:
        queue.enqueue(node.right)
    elif node.left:
        queue.enqueue(node.left)
    
while len(stack) > 0:
    node = stack.pop()
    traversal += str(node.value) + "-"
return traversal         


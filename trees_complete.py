class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    
    def __len__(self):
        return len(self.items)
    
    def size(self):
        return len(self.items)

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value
    
    def __len__(self):
        return len(self.items)
    
    def size(self):
        return len(self.items)

class Tree(object):
    def __init__(self,root):
        self.root = Node(root)

    def traversal_type(self, traverse_type):

        if traverse_type == "inorder":
            return self.in_order_traverse(tree.root, "")
        elif traverse_type == "preorder":
            return self.pre_order_traverse(tree.root,"")
        elif traverse_type == "postorder":
            return self.post_order_traverse(tree.root, "")
        elif traverse_type == "levelorder":
            return self.level_order_traverse(tree.root)
        elif traverse_type == "reverse_levelorder":
            return self.reverse_order_traverse(tree.root)
        


    def pre_order_traverse(self,start,traversal):
        if start:
            traversal += str(start.value) + "-"
            traversal = self.pre_order_traverse(start.left,traversal)
            traversal = self.pre_order_traverse(start.right,traversal)
        return traversal
    

    def post_order_traverse(self,start,traversal):
        if start:        
            traversal = self.post_order_traverse(start.left,traversal)
            traversal = self.post_order_traverse(start.right,traversal)
            traversal += str(start.value) + "-"
        return traversal

    def in_order_traverse(self,start,traversal):
        if start:
            traversal = self.in_order_traverse(start.left,traversal)
            traversal += str(start.value) + "-"
            traversal = self.in_order_traverse(start.right,traversal)
        return traversal
    

    def level_order_traverse(self, start):
        if start is None:
            return 

        traversal = ""
        queue = Queue()
        queue.enqueue(start)
        while len(queue) > 0:
            traversal += (str(queue.peek()) + "-")
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
            
        return traversal
    
    def reverse_order_traverse(self,start):

        stack = Stack()
        queue = Queue()
        traversal = ""
        queue.enqueue(start)
        

        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)
        
        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"
            
        return traversal
    
    def height(self,node):

        if node is None:
            return -1

        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return 1 + max(left_height, right_height)

    def size(self, node):
        if node is None:
            return 0

        left_nodes = self.size(node.left)
        right_nodes = self.size(node.right)
        return 1 + left_nodes + right_nodes

tree = Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# print(tree.size())
print(tree.size(tree.root))

# tree = Tree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)

# print(tree.height(tree.root))

# tree = Tree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)

# print(tree.traversal_type("reverse_levelorder"))

# tree = Tree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)

# print(tree.traversal_type("levelorder"))



# tree = Tree(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)

# #print(tree.print_tree("preorder"))
# #print(tree.print_tree("inorder"))
# print(tree.traversal_type("postorder"))
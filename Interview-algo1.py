#  4
# / \
# 2   5
# /\
# 1 3
# /
# 0
# key - 7
# output - 4-2-1

# traverse through the tree using pre-order traversal
# keep track of all the node values traversed in a list
# sum up the values as and when they are appended to the list.
# display the output path when the summed value equals key.
# continue the search for all paths.

class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = self.right = 0
    
class BST(object):
    def __init__(self,root):
        self.root = root
    
    def insert(self,new_val):
        self.insert_helper(self.root, new_val)
    
    def insert_helper(self, current, new_val):
        if current.data < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:    
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)


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

def pre_order_traverse(root):
    return pre_order_helper(root,"")
    
def pre_order_helper(current,traversal,key=8):
    sum_value = 0
    queue = Queue()
    path = ""
    if current:
        # traversal += str(current.data) 
        traversal += str(current.data)
        queue.enqueue(traversal)
        # sum_value +=  in_traverse
        traversal = pre_order_helper(current.left,traversal)
        traversal = pre_order_helper(current.right,traversal)
    # return traversal
    while not queue.is_empty():
        
        if sum_value == key:
            break
        else:
            node = queue.peek()
            sum_value += node
    return sum_value
      

# bst = BST(10)
# bst.insert(3)
# bst.insert(1)
# bst.insert(25)
# bst.insert(9)
# bst.insert(13)
root = Node(7)
bst = BST(root)
bst.insert(3)
bst.insert(10)
bst.insert(5)
bst.insert(1)
bst.insert(8)
bst.insert(9)
bst.insert(2)
print(pre_order_traverse(root))
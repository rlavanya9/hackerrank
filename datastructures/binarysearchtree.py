class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)


    def insert_BST(self, val):
        self.insert_BST_helper(self.root, val)

    def insert_BST_helper(self, current, val):
        if current < val:
            if current.right:
                self.insert_BST_helper(self, current.right, val)
            else:
                current.right = Node(val)
        else:
            if current.left:
                self.insert_BST_helper(self, current.left, val)
            else:
                current.left = Node(val)

    def search_BST(self, find_val):
        return self.search_BST_helper(self.root, find_val)

    def search_BST_helper(self, current, find_val):
        if current:
            if current.data == find_val:
                return current
            elif current.data < find_val:
                return self.search_BST_helper(self, current.right,find_val)
            else:
                return self.search_BST_helper(self, current.left,find_val)
            

    def is_BST(self):
        def is_BST_helper(self, node, lower=float('-inf'), high=float('inf')):


            val = node.data
            if val <= lower or val >= high:
                return False
            
            if not is_BST_helper(node.right, val, high):
                return False
            if not is_BST_helper(node.left, lower, val):
                return False
            return True
        return is_BST_helper(self.root)


bst = BST(10)
bst.insert_BST(3)
bst.insert_BST(1)
bst.insert_BST(25)
bst.insert_BST(9)
bst.insert_BST(13)

print(bst.search_BST(9))
print(bst.search_BST(14))
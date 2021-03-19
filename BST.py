class Node(object):
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BST(object):
    def __init__(self, root):
        self.root = Node(root)

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

    def search(self, find_val):
        return self.search_helper(self.root, find_val)
    
    def search_helper(self, current, find_val):
        if current:
            if current.data == find_val:
                return True
            elif current.data < find_val:
                return self.search_helper(current.right,find_val)
            else:
                return self.search_helper(current.left,find_val)

    def is_BST(self):
        return self.is_BST_helper(self.root, lower = float("-inf"), upper=float("inf"))
    
    def is_BST_helper(self, node, lower, upper):

        if not node:
            return True
        
        val = node.data
        if val <= lower or val >= upper:
            return False
        
        if not self.is_BST_helper(node.right, val, upper):
            return False
        if not self.is_BST_helper(node.left, lower, val):
            return False
        
        return True
    
    def delete_node(self.root,key):
        curr = self.root
        parent = None

        while curr and curr.data != key:
            parent = curr

            if curr > key:
                curr = curr.left
            else:
                curr = curr.right

            if curr.data is None:
                return root
            
            if curr.left is None and curr.right is None:
                if curr != root:
                    if parent.left == key:   
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    root = None
            
            elif curr.left and curr.right:
                succ = min_val(curr.right)
                val = succ
                delete_node(root, succ)
                curr = val
            else:
                if curr != root:
                    if parent.left == key:                 
                        parent.left = curr
                    else:
                        parent.right = curr

                else:
                    root = curr
        return root
# bst = BST(4)
# bst.insert(2)
# bst.insert(8)
# bst.insert(5)
# bst.insert(10)

# tree = BST(1)
# tree.root.left = Node(2)
# tree.root.right = Node(3)
# tree.root.left.left = Node(4)
# tree.root.left.right = Node(5)
# tree.root.right.left = Node(6)
# tree.root.right.right = Node(7)
# tree.root.right.right.right = Node(8)

# print(bst.is_BST())
# print(tree.is_BST())

# bst = BST(10)
# bst.insert(3)
# bst.insert(1)
# bst.insert(25)
# bst.insert(9)
# bst.insert(13)

# print(bst.search(9))
# print(bst.search(14))
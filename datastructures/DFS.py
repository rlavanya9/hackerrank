Class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

Class Root(object):
    def __init__(self,root):
        self.root = Node(root)

    def print_value(self, start, traversal):
        if traversal_type == "post-order traversal":
            return self.print_post_order(self, start.value, "")
        elif traversal_type == "in-order-traversal":
            return self.print_in_order(self, start.value, "")
        elif traversal_type == "pre-order-traversal":
            return self.print_pre_order(self, start.value, "")
    
    def print_post_order(self, self.value, traversal):
        if start:

            traversal = self.print_post_order(self.left.value, traversal)
            traversal = self.print_post_order(self.right.value, traversal)
            traversal += (str(self.start.value) + "-")
        return  traversal

    


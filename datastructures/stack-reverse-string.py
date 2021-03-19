class Stack(object):
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            self.items.pop()
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def __len__(self):
        return len(self.items)
    
    def size(self):
        return len(self.items)

def reverse_string(mystr):
    stack = Stack()
    rev_str = ""
    for letter in mystr:
        stack.push(letter)
    
    while not stack.is_empty():
        rev_str += stack.peek()
        stack.pop()
    return rev_str

print(reverse_string("!evitacudE ot emocleW"))

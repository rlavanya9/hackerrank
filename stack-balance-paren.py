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
    
def is_paren_balanced(mystr):
    open_paren = ['{','[','(']
    close_paren = [ ']', '}', ')']
    stack = Stack()

    for paren in mystr:
        if paren in open_paren:
            stack.push(open_paren)
        elif paren in close_paren:
            if not stack.is_empty():
                stack_pk = stack.peek()
                is_match(stack_pk,paren)
                stack.pop()
            else:
                return False

    return stack.is_empty()

def is_match(p1, p2):
    if (p1 == '{' and p2 == '}'):
        return True
    elif(p1 == '(' and p2 == ')'):
        return True
    elif(p1 == '[' and p2 == ']'):
        return True
    else:
        return False


print(is_paren_balanced("(((({}))))"))
print(is_paren_balanced("[][]]]"))
print(is_paren_balanced("[][]"))
print(is_paren_balanced("))"))



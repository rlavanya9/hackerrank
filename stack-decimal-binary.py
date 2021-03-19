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

def decimal_binary(num):
    stack = Stack()
    output = ""
    quot = 0
    remainder = 0
    if num > 0: 
        if num < 2:
            remainder = 1
            stack.push(remainder)
        else:
            quot = num//2
            remainder = num%2
            stack.push(remainder) 
            # print(stack.items)
            decimal_binary(quot)
    return stack.items
    # else:
    #     while not stack.is_empty():
    #         output += str(stack.peek())
    #         stack.pop()
    #     return output
    
print(decimal_binary(242))
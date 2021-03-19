def DFS(self, data):
    to_visit = [self]

    while to_visit:
        current = to_visit.pop()
        if current == data:
            return current
        to_visit.extend(current.children)

def BFS(self, data):
    to_visit = [self]

    while to_visit:
        current = to_visit.pop(0)
        if current == data:
            return current
        to_visit.extend(current.children)
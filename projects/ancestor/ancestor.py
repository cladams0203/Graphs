
class Queue:
    def __init__(self):
        self.q = []

    def size(self):
        return len(self.q)

    def enqueue(self, value):
        self.q.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.q.pop()
        else:
            return None

def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    path = [starting_node]
    q.enqueue(path)
    visited = set()
    while q.size() > 0:
        cur = q.dequeue()
        neighbor = []
        for i in cur:
            for j in ancestors:
                if j[1] == i and i not in visited:
                    visited.add(i)
                    neighbor.append(j[0])
                    q.enqueue(neighbor)
        if len(neighbor) <= 0:
            if  cur[0] == starting_node:
                return -1
            else:
                return cur[0]
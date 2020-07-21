"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()
        """
        Add a vertex to the graph.
        """
        # TODO

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
        """
        Add a directed edge to the graph.
        """
        # TODO

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
        """
        Get all neighbors (edges) of a vertex.
        """
        # TODO

    def bft(self, starting_vertex):
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)

        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                print(v)
                for next_v in self.get_neighbors(v):
                    q.enqueue(next_v)
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # TODO

    def dft(self, starting_vertex):
        s = Stack()
        visited = set()
        s.push(starting_vertex)
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(v)
                for next_v in self.get_neighbors(v):
                    s.push(next_v)
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # TODO

    def dft_recursive(self, starting_vertex):
        s = Stack()
        visited = set()
        def inner_dft(current):
            if current == None:
                return
            else:
                if current not in visited:
                    print(current)
                    visited.add(current)
                    for next_v in self.get_neighbors(current):
                        s.push(next_v)
                    inner_dft(s.pop())
                else:
                    inner_dft(s.pop())
        inner_dft(starting_vertex)
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # TODO

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
        q.enqueue([starting_vertex])
        visited = set()
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                visited.add(v)
                if v == destination_vertex:
                    return path
                for next_v in self.get_neighbors(v):
                    q.enqueue(path + [next_v])


        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # TODO

    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        s.push([starting_vertex])
        visited = set()
        while s.size() > 0:
            path = s.pop()
            v = path[-1]
            if v not in visited:
                visited.add(v)
                if v == destination_vertex:
                    return path
                for next_v in self.get_neighbors(v):
                    s.push(path + [next_v])
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        stack = Stack()
        visited = set()
        stack.push([starting_vertex])

        def dft_inner(current_path):
            current_vertex = current_path.pop()
            current_path.append(current_vertex)
            if current_vertex == destination_vertex:
                return current_path
            else:
                if current_vertex not in visited:
                    visited.add(current_vertex)
                    for neighbor in self.get_neighbors(current_vertex):
                        path_to_add = current_path + [neighbor]
                        stack.push(path_to_add)
                    return dft_inner(stack.pop())
                else:
                    return dft_inner(stack.pop())

        return dft_inner([starting_vertex])
"""
Return a list containing a path from
starting_vertex to destination_vertex in
depth-first order.

This should be done using recursion.
"""
# TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))

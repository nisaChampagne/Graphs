"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()
        # order doesnt matter, undirected, and very fast

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist.")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
        #vertex is same as nodes

    def get_ancestors(self, starting_vertex):
        # Do a DFS (storing the path)
        # returns their earliest known ancestor
        #  – the one at the farthest distance from the input individual
        #* Good if you are solving problems where you know the solution is very far from the root node
        stack = Stack()
        stack.push([starting_vertex])
        max_path_len = 1
        earliest_ancestor = -1

        while stack.size() > 0:
            path = stack.pop()
            v = path[-1]

            # If the path is longer or equal and the value is smaller, or if the path is longer
            if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
                earliest_ancestor = v
                max_path_len = len(path)
            for neighbor in self.vertices[v]:
                new_path = list(path)
                new_path.append(neighbor)
                stack.push(new_path)
        return earliest_ancestor

    def bft(self, starting_vertex): # QUEUE IS FIFO
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
       
        # Create an empty queue
        queue = Queue()
        # Add the starting vertex_id to the queue
        queue.enqueue(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while queue.size() > 0:
            # Dequeue, the first vertex
            v = queue.dequeue()
            # Check if it's been visited
            if v not in visited:
            # If it has not been visited...
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all neighbors to the back of the queue
                for neighbor in self.vertices[v]:
                    queue.enqueue(neighbor)



    def dft(self, starting_vertex): # STACK IS LIFO
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #create empty stack
        stack = Stack()
          # Add the starting vertex_id to the stack
        stack.push(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty...
        while stack.size() > 0:
            # pop the first vertex
            v = stack.pop()
            # Check if it's been visited
            if v not in visited:
            # If it has not been visited...
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all neighbors to the top of the stack
                for neighbor in self.vertices[v]:
                    stack.push(neighbor)


    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            # Create an empty set to store visited nodes
            visited = set()
        # adding starting_vertex to empty set
        visited.add(starting_vertex)
        #looping through
        for next_vertex in self.vertices[starting_vertex]:
            # if next_vertex not visited
            if next_vertex not in visited:
                # recurse through
                self.dft_recursive(next_vertex, visited)
                # without visited, infinite loop happens!


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #searching for another node
        #want to return a path from 1 to 6 for example

        # Create an empty queue
        q = Queue()
        # Add A PATH TO the starting vertex_id to the queue
        q.enqueue([starting_vertex]) 
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH
            path = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            vertex = path[-1]
            # Check if it's been visited
            # If it has not been visited...
            if vertex not in visited:
                # check if it is the target(destination_vertex)
                # if so, return path
                if vertex == destination_vertex:
                    return path
                # Mark it as visited
                visited.add(vertex)
                # Then add A PATH TO all neighbors to the back of the stack
                for neighbor in self.get_neighbors(vertex):
                    # make copy of the path before adding
                    new_path = list(path)
                    #append neighbor to new_path copy
                    new_path.append(neighbor)
                    # add new_path to q 
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """

        # Create an empty stack
        stack = Stack()
        # Add A PATH TO the starting vertex_id to the stack
        stack.push([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty...
        while stack.size() > 0:
            # pop the first PATH
            path = stack.pop()
            # GRAB THE LAST VERTEX FROM THE PATH
            vertex = path[-1]
            # Check if it's been visited
            # If it has not been visited...
            if vertex not in visited:
                # check if it is the target(destination_vertex)
                # if so, return path
                if vertex == destination_vertex:
                    return path
                # Mark it as visited
                visited.add(vertex)
                # Then add A PATH TO all neighbors to the back of the stack
                    # make copy of the path before adding
                for neighbor in self.get_neighbors(vertex):
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.push(new_path)

        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # base cases
        if visited is None:
            #initialize
            visited = set()
        if path is None:
            #initialize
            path = []
        visited.add(starting_vertex)
        # path is = to empty list + the next item to check via DFS 
        path = path + [starting_vertex]
        # print(path, 'path')
        # print([starting_vertex], 'starting vertex')
        #if starting_vertex is the destination_vertex 
        if starting_vertex == destination_vertex:
            #return path that gets to destination_vertex
            return path
        for neighbor in self.vertices[starting_vertex]:
            if neighbor not in visited:
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if new_path:
                    return new_path
        return None


# if __name__ == '__main__':
#     graph = Graph()  # Instantiate your graph
#     # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)
#     graph.add_vertex(4)
#     graph.add_vertex(5)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_edge(5, 3)
#     graph.add_edge(6, 3)
#     graph.add_edge(7, 1)
#     graph.add_edge(4, 7)
#     graph.add_edge(1, 2)
#     graph.add_edge(7, 6)
#     graph.add_edge(2, 4)
#     graph.add_edge(3, 5)
#     graph.add_edge(2, 3)
#     graph.add_edge(4, 6)

#     '''
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
#     print(graph.vertices)

#     # '''
#     # Valid BFT paths:
#     #     1, 2, 3, 4, 5, 6, 7
#     #     1, 2, 3, 4, 5, 7, 6
#     #     1, 2, 3, 4, 6, 7, 5
#     #     1, 2, 3, 4, 6, 5, 7
#     #     1, 2, 3, 4, 7, 6, 5
#     #     1, 2, 3, 4, 7, 5, 6
#     #     1, 2, 4, 3, 5, 6, 7
#     #     1, 2, 4, 3, 5, 7, 6
#     #     1, 2, 4, 3, 6, 7, 5
#     #     1, 2, 4, 3, 6, 5, 7
#     #     1, 2, 4, 3, 7, 6, 5
#     #     1, 2, 4, 3, 7, 5, 6
#     # '''
#     graph.bft(1)

#     # '''
#     # Valid DFT paths:
#     #     1, 2, 3, 5, 4, 6, 7
#     #     1, 2, 3, 5, 4, 7, 6
#     #     1, 2, 4, 7, 6, 3, 5
#     #     1, 2, 4, 6, 3, 5, 7
#     # '''
#     graph.dft(1)
#     graph.dft_recursive(7)

#     # '''
#     # Valid BFS path:
#     #     [1, 2, 4, 6]
#     # '''
#     print(graph.bfs(1, 6))

#     # '''
#     # Valid DFS paths:
#     #     [1, 2, 4, 6]
#     #     [1, 2, 4, 7, 6]
#     # '''
#     print(graph.dfs(1, 6))
#     print(graph.dfs_recursive(1, 6), 'this one')
#     print(graph.dfs_recursive(1, 7), 'test one')

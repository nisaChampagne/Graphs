'''

Here are steps to solve (almost) any graph problems:

1) Translate the problem into graph terminology
	* what are my nodes and edges
		* nodes are parents and children
		* edges/neighbors:  relationships over multiple generations
	* is this a directed, undirected, cyclic, acyclic, dense, sparse
		* undirected because both parent and child  are related to each other
		* cyclic
		* sparse
	
2) Build your graph
3) Traverse your graph


'''

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


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

def earliest_ancestor(ancestors, starting_node):
    pass
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
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    ancestor_graph = Graph()

    for ancestor in ancestors:
        ancestor_graph.add_vertex(ancestor[0])
        ancestor_graph.add_vertex(ancestor[1])

    for ancestor in ancestors:
        ancestor_graph.add_edge(ancestor[1], ancestor[0])

    return ancestor_graph.get_ancestors(starting_node)


# ```
#  10
#  /
# 1   2   4  11
#  \ /   / \ /
#   3   5   8
#    \ / \   \
#     6   7   9
# ```

# If the input individual has no parents, the function should return -1.
#parent    child
# 1:        {3}
# 2:        {3}
# 3:        {6}
# 5:        {6}
# 5:        {7}
# 4:        {5}
# 4:        {8}
# 8:        {9}
# 11:       {8}
# 10:       {1}

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors, 1))
print(earliest_ancestor(test_ancestors, 2))
print(earliest_ancestor(test_ancestors, 3))
print(earliest_ancestor(test_ancestors, 4))
print(earliest_ancestor(test_ancestors, 5))
print(earliest_ancestor(test_ancestors, 6))
print(earliest_ancestor(test_ancestors, 7))
print(earliest_ancestor(test_ancestors, 8))
print(earliest_ancestor(test_ancestors, 9))






                    


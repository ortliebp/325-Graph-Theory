# Author: Pierce Ortlieb
# Title: Bipartitie Graphs & Matchings
# About: Python script will find matchings of a graph and determine if bipartite

# Find the power set of a given set
def power(set):
    power_set = []
    # Iterate over our initial list
    for item in set:
        # Iterate over each sub set of our in-progress powerset
        for sub_set in power_set:
                # Check to make sure we dont end up with something like ABB or BCCC
                if item not in sub_set:
                    power_set.append(list(sub_set) + list(item))
        # Append our single values such as A, B, C
        power_set.append(list(item))
    # Sort our power set by length
    power_set.sort(key=len)
    # Empty set is always part of a power set
    return power_set

# Input a bipartite graph and find its partitie sets
def partite_sets(graph):
    partite_sets = []
    # Iterate through values of graph
    for key, value in graph.items():
            # Add the set if not already in the partite set
            if value not in partite_sets:
                partite_sets.append(value)
    return partite_sets

# Input a bipartite graph and return true if a perfect matching 
def is_perfect(graph):
    # Get parite sets of the given graph
    partite_set = partite_sets(graph)
    for x in partite_set:
        # Find all subsets of selected partite set
        power_set = power(x)
        for vertex in power_set:
            neighbors = []
            # Find vertices adjacent to the vertex
            for v in vertex:
                neighbors.append(graph.get(v))
            # Check if the neighborhood of a vertex is smaller than the subset of the partite set
            if len(neighbors) < len(vertex):
                return False  
    # If there was not a neighborhood smaller than the size of the subset, for all subsets of the partite sets we return True                  
    return True

# Input a graph and return true if bipartite
def is_bipartite(graph):
    temp = partite_sets(graph)
    print(temp)
    # If the partite set is longer than 2 we know that the graoh cannot be bipartite
    if len(partite_sets(graph)) <= 2:
        return True
    else:
        return False

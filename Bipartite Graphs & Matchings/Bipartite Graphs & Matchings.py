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
    power_set.insert(0, list(' '))
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
    set_builder = []
    for key in graph.keys():
        for value in graph.items():
            if key in value[1]:
                set_builder.append(key)
                if set_builder == graph.keys():
                    return True
                    print(set_builder)
                    print(graph.keys)

temp_perf_graph = {'A' :['B', 'C'], 'B' :['A', 'D'], 'C' :['A', 'D'], 'D' :['B', 'C']}
# temp_notperf_graph = {'A' : ['B', 'C'], 'B' : ['A'], 'C' : ['A']}
is_perfect(temp_perf_graph)

# Input a graph and return true if bipartite
# def is_bipartite(graph):
#     print("is bipartite")


# Author: Pierce Ortlieb
# Title: Bipartitie Graphs & Matchings
# Date: 11/29/17

# Find the power set of a given list
def power(list):
    set = list
    sets = []
    # Iterate over our initial list
    for item in set:
        # Iterate over each set in sets
        for set in sets:
            sets.append(set + item)
        sets.append(item)
    sets.append(" ")

temp = ["A", "B"]
power(temp)


# def partite_sets(graph):
#     print("partite")

# def is_perfect(graph):
#     print("is perfect")

# def is_bipartite(graph):
#     print("is bipartite")


# Search methods

import search

mg = search.GPSProblem('M', 'G'
                       , search.romania)

print("\nRamificación y Acotación")
print(search.RyA_graph_search(mg).path())
print("\nRamificación y Acotación con Subestimación")
print(search.RyAsub_graph_search(mg).path())

print("\n******************************************************************************")

oe = search.GPSProblem('O', 'E'
                       , search.romania)

print("\nRamificación y Acotación")
print(search.RyA_graph_search(oe).path())
print("\nRamificación y Acotación con Subestimación")
print(search.RyAsub_graph_search(oe).path())

print("\n******************************************************************************")

ht = search.GPSProblem('H', 'T'
                       , search.romania)

print("\nRamificación y Acotación")
print(search.RyA_graph_search(ht).path())
print("\nRamificación y Acotación con Subestimación")
print(search.RyAsub_graph_search(ht).path())

print("\n******************************************************************************")

ag = search.GPSProblem('A', 'G'
                       , search.romania)

print("\nRamificación y Acotación")
print(search.RyA_graph_search(ag).path())
print("\nRamificación y Acotación con Subestimación")
print(search.RyAsub_graph_search(ag).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450

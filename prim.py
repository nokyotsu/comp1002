#!/usr/bin/env python3
from collections import defaultdict

def add_edge(graph, u, v, cost):
  graph[u][v] = cost
  graph[v][u] = cost
  return graph

def print_graph(graph):
  for u in sorted(graph.keys()):
    for v in sorted(graph[u].keys()):
      if u < v:
        print('({0},{1}) - {2}'.format(u, v, graph[u][v]))

def pick_node(graph):
  return sorted(graph.keys())[0]

def Prim(graph):
  solution = defaultdict(dict)
  nearest = { }
  a = pick_node(graph)
  for b, cost_ab in graph[a].items():
    nearest[b] = (a, cost_ab)
  while nearest:
    # find candidate edge with minimum cost
    u, v, cost_uv = None, None, None
    for x, (y, cost_xy) in nearest.items():
      if cost_uv is None or cost_xy < cost_uv:
        u, v, cost_uv = x, y, cost_xy
    # add edge to solution
    add_edge(solution, u, v, cost_uv)
    del nearest[u]
    # add new edges if nearest to u
    for w, cost_uw in graph[u].items():
      if w in solution:
        continue
      if not w in nearest or cost_uw < nearest[w][1]:
        nearest[w] = (u, cost_uw)
  return solution

graph = defaultdict(dict)
add_edge(graph, 'a', 'b', 1)
add_edge(graph, 'a', 'd', 4)
add_edge(graph, 'b', 'c', 2)
add_edge(graph, 'b', 'd', 6)
add_edge(graph, 'b', 'e', 4)
add_edge(graph, 'c', 'e', 5)
add_edge(graph, 'c', 'f', 6)
add_edge(graph, 'd', 'e', 3)
add_edge(graph, 'd', 'g', 5)
add_edge(graph, 'e', 'f', 8)
add_edge(graph, 'e', 'g', 7)
add_edge(graph, 'f', 'g', 3)
print("Input")
print_graph(graph)
print("Output")
print_graph(Prim(graph))

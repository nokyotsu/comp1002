#!/usr/bin/env python3
from collections import defaultdict

class Graph:
  adj_list = defaultdict(dict)
  
  def add_edge(self, u, v, c):
    """
      Add an undirected edge between `u` and `v` with cost `c`
    """
    self.adj_list[u][v] = c
    self.adj_list[v][u] = c
    return self
    
  def has_edge(self, u, v):
    """
      Test whether the edge (u,v) exists in the graph
    """
    return u in self.adj_list and v in self.adj_list[u]

  def cost(self, u, v):
    """
      Return the cost of the edge (u, v); or None if the edge does not exist
    """
    if self.has_edge(u, v):
      return self.adj_list[u][v]
    else:
      return None
  
  def nodes(self):
    """
      Return a list of the nodes in the graph
    """
    return list(self.adj_list.keys())
    
  def adjacent(self, u):
    """
      Return a list of the nodes adjacent to the node `u`
    """
    return list(self.adj_list[u].keys())
  
  def __str__(self):
    edges = []
    for u in self.nodes():
      for v in self.adjacent(u):
        if u < v:
          edges.append('({0}, {1}):{2}'.format(u, v, self.adj_list[u][v]))
    return '[' + ', '.join(edges) + ']'

def Prim(graph):
  """
    Returns the minimum spanning tree of the input graph; the tree
    is represented as a "parent-of" dictionary.
    
    The nearest edges, also represented using a dictionary, always maps a node
    *outside* of the current spanning tree to its nearest node *inside* of the
    tree with a non-infinite cost.
  """
  span_tree = { }
  nearest = { }
  nodes = graph.nodes()
  y = nodes.pop()
  for x in nodes:
    if graph.has_edge(x, y):
      nearest[x] = y
  while nearest:
    # find new edge with minimum cost
    u, v, c = None, None, None
    for x, y in nearest.items():
      cost_xy = graph.cost(x,y)
      if c is None or cost_xy < c:
        u, v, c = x, y, cost_xy
    # remove from near edges and add to spanning tree
    del nearest[u]
    span_tree[u] = v
    nodes.remove(u)
    # update nearest edges to u
    for x in nodes:
      if graph.has_edge(x,u):
        if x in nearest:
          w = nearest[x]
          if graph.cost(x,u) < graph.cost(x,w):
            nearest[x] = u
        else:
          nearest[x] = u
  return span_tree

g1 = Graph()
g1.add_edge('a', 'b', 1)
g1.add_edge('a', 'd', 4)
g1.add_edge('b', 'c', 2)
g1.add_edge('b', 'd', 6)
g1.add_edge('b', 'e', 4)
g1.add_edge('c', 'e', 5)
g1.add_edge('c', 'f', 6)
g1.add_edge('d', 'e', 3)
g1.add_edge('d', 'g', 5)
g1.add_edge('e', 'f', 8)
g1.add_edge('e', 'g', 7)
g1.add_edge('f', 'g', 3)
print("Input:", g1)
print("Output:", Prim(g1))

#!/usr/bin/env python3

def Floyd(C):
  n = len(C)
  for k in range(n):
    for i in range(n):
      for j in range(n):
        if C[i][k] is None or C[k][j] is None:
          continue
        new_cost = C[i][k] + C[k][j]
        if C[i][j] is None or new_cost < C[i][j]:
          C[i][j] = new_cost
  return C

C = [
  [   0,    3, None,    4, None],
  [None,    0,    4,    2,    1],
  [None, None,    0, None, None],
  [   4, None, None,    0,    3],
  [None, None,    2,    2,    0],
]

Floyd(C)

for row in C:
  print(row)

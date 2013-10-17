#!/usr/bin/env python3

def binom_table(size):
  B = [[0 for x in range(size)] for x in range(size)]
  B[0][0] = 1
  for n in range(1, size):
    B[n][0] = 1
    for k in range(1, n):
      B[n][k] = B[n - 1][k - 1] + B[n - 1][k]
    B[n][n] = 1
  return B

B = binom_table(9)
for n in range(9):
  for k in range(n + 1):
    print(B[n][k], end=' ')
  print()

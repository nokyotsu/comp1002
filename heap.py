#!/usr/bin/env python3

def heap_insert(H, x):
  i = len(H)
  H.append(x)
  while i > 0:
    p = (i - 1) // 2
    if H[p] < H[i]:
      break
    (H[p], H[i]) = (H[i], H[p])
    i = p

A = [94,65,39,75,56,93,55,21,38,33]
H = []
for x in A:
  heap_insert(H, x)
print(H)

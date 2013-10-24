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
    
def heap_delete(H):
  (H[0], H[-1]) = (H[-1], H[0])
  min = H.pop()
  p = 0
  while p < len(H):
    i = 2*p + 1                            # i = the left child of p
    if i >= len(H): break                  # if there is no left child
    if i + 1 < len(H) and H[i + 1] < H[i]: # if the right child is smaller
      i = i + 1                            #   i = the right child of p
    if H[p] < H[i]:                        # if the parent is smaller
      break
    (H[p], H[i]) = (H[i], H[p])
    p = i
  return min

A = [94,65,39,75,56,93,55,21,38,33,27]
H = []
for x in A:
  heap_insert(H, x)
print(H)
while H:
  x = heap_delete(H)
  print(x, H)

#!/usr/bin/env python3

def partition(A, i, j):
  p = i
  for k in range(i, j):
    if A[k] < A[j]:
      (A[p], A[k]) = (A[k], A[p])
      p += 1
  (A[p], A[j]) = (A[j], A[p])
  return p

A = [35,15,6,30,9,43,27,16]
print(A)
p = partition(A, 0, len(A) - 1)
print("pivot:", A[p])
print(A)

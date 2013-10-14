#!/usr/bin/env python3

def merge(A, B):
    """
    Assumes that the arrays A and B are each already sorted, and merges both
    into a single sorted array C
    """
    C = [0] * (len(A) + len(B))
    i = j = k = 0
    while i < len(A) or j < len(B):
        if i < len(A) and (j >= len(B) or A[i] < B[j]):
            C[k] = A[i]
            i += 1
            k += 1
        else:
            C[k] = B[j]
            j += 1
            k += 1
    return C

A = merge([6, 15, 30, 35], [9, 16, 27, 43])
print(A)


#!/usr/bin/env python3

def InsertionSort(A):
    """Sort elements in array A"""
    for i in range(1, len(A)):
        x = A[i]
        j = i
        while 0 < j and x < A[j - 1]:
            A[j] = A[j - 1]
            j = j - 1
        A[j] = x
    return A

A = [53, 3, 42, 82, 2, 14]
print(A[2])
print(len(A))
print(InsertionSort(A))

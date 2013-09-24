#!/usr/bin/env python3

def InsertionSort(A):
	"""Sort elements in array A"""
	for j in range(1, len(A)):
		x = A[j]
		i = j
		while 0 < i and x < A[i - 1]:
			A[i] = A[i - 1]
			i = i - 1
		A[i] = x
	return A

A = [53, 3, 42, 82, 2, 14]
print(A[2])
print(len(A))
print(InsertionSort(A))

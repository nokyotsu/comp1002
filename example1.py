#!/usr/bin/env python3

def SumSquares(n):
    """Sum squares of numbers from 1 to n"""
    sum = 0
    for i in range(1, n + 1):
      sum = sum + i ** 2
    return sum

print(1, "->", SumSquares(1))
print(2, "->", SumSquares(2))
print(3, "->", SumSquares(3))
print(4, "->", SumSquares(4))
print(5, "->", SumSquares(5))
print(6, "->", SumSquares(6))

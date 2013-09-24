#!/usr/bin/env python3

def SumSquares(n):
    """Sum squares of numbers from 1 to n"""
    sum = 0
    while n > 0:
      sum = sum + n ** 2
      n = n - 1
    return sum

n = 6
print(SumSquares(n))
print(n)
print("---")
print(1, "->", SumSquares(1))
print(2, "->", SumSquares(2))
print(3, "->", SumSquares(3))
print(4, "->", SumSquares(4))
print(5, "->", SumSquares(5))
print(6, "->", SumSquares(6))

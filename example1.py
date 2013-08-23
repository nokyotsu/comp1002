#!/usr/bin/env python3

def SumSquares(n):
    """Sum squares of numbers from 1 to n"""
    sum = 0
    for i in range(1, n + 1):
      sum = sum + i ** 2
    return sum

print(SumSquares(1))
print(SumSquares(2))
print(SumSquares(3))
print(SumSquares(4))
print(SumSquares(5))
print(SumSquares(6))

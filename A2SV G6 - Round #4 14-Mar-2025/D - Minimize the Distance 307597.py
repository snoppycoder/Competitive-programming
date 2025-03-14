# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

from sys import stdin
import math
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]
n = int(inp())
nums = ls()
nums.sort()

index = n//2
if n % 2 == 0:

    print(nums[index-1])
else:
    print(nums[index])


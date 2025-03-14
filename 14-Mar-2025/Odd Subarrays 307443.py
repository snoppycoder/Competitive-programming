# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]
t = int(inp())
for _ in range(t):
    n = int(inp())
    arr = ls()
    res = 0
    left  = 0
    right = left+1
    while right < n:
        if arr[left] > arr[right]:
            res += 1
            left += 2
            right = left+1 
        else:
            left += 1
            right+=1
    
    print(res)
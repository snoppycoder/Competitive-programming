# Problem: Books - https://codeforces.com/contest/279/problem/B

from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]
n, t = ls()
nums = ls()
left = 0
total = 0

res = float('-inf')
for right in range(len(nums)):
    total += nums[right]
    while total > t:
        total-=nums[left]
        left+=1
    res = max(res, right-left+1)
print(res)
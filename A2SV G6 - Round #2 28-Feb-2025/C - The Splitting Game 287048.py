# Problem: C - The Splitting Game - https://codeforces.com/gym/586960/problem/C

from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]
from collections import Counter, defaultdict
t = int(input())
for _ in range(t):
    n = int(inp())
    word= inp()
    res = 0
    a, b =  Counter(), Counter(word)

    for char in word:
        b[char] -= 1
        if b[char] == 0:
            del b[char]
        a[char] +=1
        res = max(res, len(b) + len(a))
    print(res)
        

        



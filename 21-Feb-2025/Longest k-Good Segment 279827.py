# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict
from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]

def longest_k_good_segment(n, k, a):
    count = defaultdict(int)
    left = 0
    distinct_count = 0
    max_len = 0
    best_l, best_r = 0, 0

    for right in range(n):
 
        if count[a[right]] == 0:
            distinct_count += 1
        count[a[right]] += 1

       
        while distinct_count > k:
            count[a[left]] -= 1
            if count[a[left]] == 0:
                distinct_count -= 1
            left += 1 

        
        if right - left + 1 > max_len:
            max_len = right - left + 1
            best_l, best_r = left, right

    
    print(best_l + 1, best_r + 1)



n, k = ls()
a = ls()
longest_k_good_segment(n, k, a)
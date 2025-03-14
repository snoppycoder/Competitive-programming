# Problem: B - Anansi and Trip-Photographs - https://codeforces.com/gym/588468/problem/B

from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]
t = int(input())
def ans(nums, x):
    right= len(nums)//2
    left = 0
    while(right < len(nums)):
        if(nums[right] - nums[left] >= x):
            left+=1
            right+=1
        else:
            return False
    return True

for _ in range(t):
    n, x = ls()
    nums = ls()
    nums.sort()
   
    if ans(nums, x):
        print("YES")
    else:
        print("NO")
   
        
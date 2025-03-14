# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]
n, m = ls()
nums = ls()
forward = [0]*n
backward = [0]*(n)
for i in range(1, len(nums)):
    forward[i] = forward[i-1]
    if nums[i] < nums[i-1]:
        forward[i] = -nums[i] + nums[i-1] + forward[i-1]
    
nums2 = nums[::-1]
for i in range(1, len(nums2)):
    backward[i] = backward[i-1]
    if nums2[i] < nums2[i-1]:
        backward[i] = -nums2[i] + nums2[i-1] + backward[i-1]
   
   

backward.reverse()
q = []


for _ in range(m):
    f = ls()
    q.append(f)
for left, right in q:
    if left < right:
        print(forward[right-1] - forward[left-1])

    else:
        print(backward[right-1] - backward[left-1])





# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

from sys import stdin
def inp(): return stdin.readline().strip()
def ls(): return [int(i) for i in inp().split()]
def mt(rows): return[list(map(int, inp().split())) for _ in range(rows)]
t = int(inp())
for _ in range(t):
    n = int(inp())
    s = inp()
    i = 0
    ans = []
    stack0 = []
    stack1 = []
    for num in s:
        # z = 0
        # o = 0
        if num == "0":
            if not stack1:
                i += 1
                # print(i,"0")
                stack0.append(i)
                
            else:
                stack0.append(stack1.pop())
            ans.append(stack0[-1])
        else:
            if not stack0:
                i += 1
                # print(i,"1")
                stack1.append(i)
            else:
                stack1.append(stack0.pop())
            ans.append(stack1[-1])


    print(i)
    print(*(ans))
            

    
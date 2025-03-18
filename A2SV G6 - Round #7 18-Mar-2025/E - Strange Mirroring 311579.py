# Problem: E - Strange Mirroring - https://codeforces.com/gym/596141/problem/E

t = int(input())

for _ in range(t):
    s = input()
    q = int(input())
    k = list(map(int, input().split()))
    
    sizes = [len(s)]
    max_ki = max(k)
    while sizes[-1] <= max_ki:
        sizes.append(2*sizes[-1])
    
    def recurse(row, i):
        if row == 0:
            return s[i - 1]
        
        cur_row_size = sizes[row]
        if i <= cur_row_size//2:
            return recurse(row - 1, i)
        else:
            prev = recurse(row - 1, i - cur_row_size//2)
            if prev.islower():
                return prev.upper()
            return prev.lower()
    
    ans = []
    for ki in k:
        for row in range(len(sizes)):
            if ki <= sizes[row]:
                ans.append(recurse(row, ki))
                break
    
    print(*ans)
        
        
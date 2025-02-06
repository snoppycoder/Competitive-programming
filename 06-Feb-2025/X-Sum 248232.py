# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def max_bishop_sum(t, test_cases):
    results = []
    
    for case in test_cases:
        n, m, grid = case
        diag1 = {}  
        diag2 = {}  
        
      
        for i in range(n):
            for j in range(m):
                d1 = i - j
                d2 = i + j
                diag1[d1] = diag1.get(d1, 0) + grid[i][j]
                diag2[d2] = diag2.get(d2, 0) + grid[i][j]
        
        max_sum = 0
       
        for i in range(n):
            for j in range(m):
                d1 = i - j
                d2 = i + j
                total_sum = diag1[d1] + diag2[d2] - grid[i][j]
                max_sum = max(max_sum, total_sum)
        
        results.append(max_sum)
    
    return results


t = int(input())
test_cases = []
for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    test_cases.append((n, m, grid))

for res in max_bishop_sum(t, test_cases):
    print(res)

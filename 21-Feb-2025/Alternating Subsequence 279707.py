# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

def max_alternating_subsequence(t, test_cases):
    results = []
    
    for n, a in test_cases:
        max_sum = 0
        current_max = a[0]
        
        for i in range(1, n):
            if (a[i] > 0) == (current_max > 0):  
                current_max = max(current_max, a[i])
            else:  
                max_sum += current_max
                current_max = a[i]
        
        max_sum += current_max 
        
        results.append(str(max_sum))
    
    print("\n".join(results))  


import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
test_cases = []
index = 1

for _ in range(t):
    n = int(data[index])
    a = list(map(int, data[index+1:index+1+n]))
    test_cases.append((n, a))
    index += n + 1

max_alternating_subsequence(t, test_cases)

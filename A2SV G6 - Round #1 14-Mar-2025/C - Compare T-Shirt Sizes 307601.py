# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585107/problem/C

def compare_sizes(a, b):
    
    if a == b:
        return "="

    if a == "M":
        return ">" if b[-1] == "S" else "<"
    if b == "M":
        return "<" if a[-1] == "S" else ">"
    
  
    if a[-1] == "S" and b[-1] == "S":
        return "<" if len(a) > len(b) else ">"
    
   
    if a[-1] == "L" and b[-1] == "L":
        return ">" if len(a) > len(b) else "<"
    
   
    return "<" if a[-1] == "S" else ">"
t = int(input())  
for _ in range(t):
    a, b = input().split()
    print(compare_sizes(a, b))

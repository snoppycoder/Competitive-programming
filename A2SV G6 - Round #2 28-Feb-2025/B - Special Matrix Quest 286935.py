# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n = int(input())
matrix = []
for _ in range(n):
    a = list(map(int, input().split() ))
    matrix.append(a)
    
res = 0
for row in range(n):
    for col in range(n):
        if(row == col):
            res += matrix[row][col]
        elif(row + col == n - 1):
            res += matrix[row][col]
        elif(col == n //2 ):
            res += matrix[row][col]
        elif(row == n//2):
            res += matrix[row][col]

print(res)
        
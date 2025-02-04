# Problem: Sum - https://codeforces.com/contest/1742/problem/A

for _ in range(int(input())):
    numbers = list(map(int, input().split()))
    n = len(numbers)
    flag = False
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or i == k or j == k:
                    continue

                if numbers[k] == numbers[i] + numbers[j]:
                    print("YES")
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
    if not flag:
        print("NO")
    
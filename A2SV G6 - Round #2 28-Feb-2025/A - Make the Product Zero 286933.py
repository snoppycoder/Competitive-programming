# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

t = int(input())
nums = list(map(int, input().split()))
print(min([abs(num) for num in nums]))
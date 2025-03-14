# Problem: A - Vus the Cossack and a Contest - https://codeforces.com/gym/585107/problem/A

n = input().split()
min_value = int(min(int(n[1]), int(n[2])))
if(min_value >= int(n[0])):
    print("Yes")
else:
    print("No")

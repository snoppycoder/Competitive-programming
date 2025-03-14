# Problem: B - Square String? - https://codeforces.com/gym/585107/problem/B

n = int(input())


for i in range(n):
    next = list(input())
    index = len(next)//2
    if(len(next) == 0):
        print("NO")
    
    if(len(next) % 2 != 0):
         print("NO")
    elif(len(next) % 2 == 0 and "".join(next[:index])== "".join(next[index:])):
       print("YES")
    else:
        print("NO")

  


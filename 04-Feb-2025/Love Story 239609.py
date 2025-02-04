# Problem: Love Story - https://codeforces.com/contest/1829/problem/A

compare = "codeforces"

for _ in range(int(input())):
    counter = 0
    word = input()
    for i in range(10):
            if(compare[i] != word[i]):
                counter+=1
    print( counter )

    

    
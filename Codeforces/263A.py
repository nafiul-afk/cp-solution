#https://codeforces.com/problemset/problem/263/A

for i in range(5):
    row = list(map(int, input().split()))
    for j in range(5):
        if row[j] == 1:
            print(abs(i + 1 - 3) + abs(j + 1 - 3))

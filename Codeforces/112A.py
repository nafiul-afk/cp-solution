# https://codeforces.com/problemset/problem/112/A

a = input().lower()
b = input().lower()

if a < b:
    print(-1)
elif a > b:
    print(1)
else:
    print(0)

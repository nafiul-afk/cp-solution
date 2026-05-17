# https://codeforces.com/problemset/problem/59/A

s = input()
u = 0
l = 0

for c in s:
    if c.isupper():
        u += 1
    else:
        l += 1

if u > l:
    print(s.upper())
else:
    print(s.lower())

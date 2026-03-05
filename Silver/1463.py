import sys

input = sys.stdin.readline

N = int(input())

dp = [0,1]
temp_li = []
least_li = []

for i in range(3, N+1):
    if i % 3 == 0:
        temp_li.append(i // 3)
    if i % 2 == 0:
        temp_li.append(i // 2)
    if (i-1) not in temp_li:
        temp_li.append(i-1)
    
    for j in temp_li:
        least_li.append(1 + dp[j-1])
    least_li.sort()
    dp.append(least_li[0])
    temp_li = []
    least_li = []

if N == 1:
    print(0)
else:
    print(dp[-1])
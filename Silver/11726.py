import sys

input = sys.stdin.readline

n = int(input())

dp = [1,2,3]
cnt = 0


for i in range(3,n):
    dp.append(dp[i-1] + dp[i-2])

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    print(dp[-1] % 10007)
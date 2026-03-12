import sys

input = sys.stdin.readline

N = int(input())

skwin = 10000000
cywin = -10000000

dp = [i for i in range(1,N+1)]

dp[0] = skwin

for i in range(1,N):
    if dp[i - 1] == skwin:
        dp[i] = cywin
    else:
        dp[i] = skwin
       
if dp[N-1] == skwin:
    print("SK")
else:
    print("CY")
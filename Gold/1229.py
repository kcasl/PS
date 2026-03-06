import sys
input = sys.stdin.readline

N = int(input())

hex_nums = []
i = 1
while i * (2*i - 1) <= N:
    hex_nums.append(i * (2*i - 1))
    i += 1

dp = [1e8] * (N+1)
dp[0] = 0

for h in hex_nums:
    
    
    
    for i in range(h, N+1):
        
        dp[i] = min(dp[i], dp[i-h] + 1)




print(dp[N])
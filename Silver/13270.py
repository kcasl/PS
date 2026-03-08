import sys

input = sys.stdin.readline

N = int(input())

people = [2, 3]
chicken = [1, 2]

while people[-1] <= N:
    people.append(people[-1] + people[-2])
    chicken.append(chicken[-1] + chicken[-2])

INF = 10**9
min_dp = [INF] * (N+1)
max_dp = [-INF] * (N+1)

min_dp[0] = 0
max_dp[0] = 0

for p, c in zip(people, chicken):
    for i in range(p, N+1):
        min_dp[i] = min(min_dp[i], min_dp[i-p] + c)
        max_dp[i] = max(max_dp[i], max_dp[i-p] + c)

print(min_dp[N], max_dp[N])
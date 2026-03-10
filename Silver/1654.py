import sys
input = sys.stdin.readline

K, N = map(int, input().split())
k_li = [int(input()) for _ in range(K)]

left = 1
right = max(k_li)
res = 0

while left <= right:
    mid = (left + right) // 2
    
    cnt = 0
    for k in k_li:
        cnt += k // mid
        
    if cnt >= N:
        res = mid
        left = mid + 1
    else:
        right = mid - 1

print(res)
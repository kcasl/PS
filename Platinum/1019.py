import sys
input = sys.stdin.readline

N = int(input())
li = [0] * 10
num = 1
def nine(N):
    while N % 10 != 9:
        for i in str(N):
            li[int(i)] += num
        N -= 1
    return N
while N > 0:
    N = nine(N)
    if N < 10:
        for i in range(N + 1):
            li[i] += num
    else:
        for i in range(10):
            li[i] += (N // 10 + 1) * num
    li[0] -= num
    num *= 10
    N //= 10
for i in range(0, 10):
    print(li[i], end=' ')
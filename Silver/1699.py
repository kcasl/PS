import sys

input = sys.stdin.readline

N = int(input())

square_li = [1]

cnt = 2

while True:
    if square_li[-1] > N:
        break
    square_li.append(cnt ** 2)
    cnt += 1
    
dp = [10e7] * (N+1)


        
        
        
import sys

input = sys.stdin.readline

N = int(input())

enjoy = 0

height_li = []

height_li.append(N)

while True:
    if all(x == 1 for x in height_li):
        break
    for i in height_li:
        if i != 1:
            h1 = i // 2
            h2 = i - h1
            height_li.remove(i)
            height_li.append(h1)
            height_li.append(h2)
            enjoy += h1 * h2
        elif i == 1:
            continue
print(enjoy)
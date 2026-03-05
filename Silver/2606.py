import sys

def infection(connection_list):
    for k in connection_list:
        if k not in infection_list:
            infection_list.append(k)

input = sys.stdin.readline

connection = {}
infection_list = []

N = int(input())
M = int(input())

for h in range(1,N+1):
    connection[str(h)] = []

for i in range(M):
    a,b = map(int,input().split())
    connection[str(a)].append(b)
    connection[str(b)].append(a)

infection(connection["1"])

for j in infection_list:
    infection(connection[str(j)])

if 1 in infection_list:
    infection_list.remove(1)

print(len(infection_list))

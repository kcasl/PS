import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):
    visited[x][y] = True
    color = graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and graph[nx][ny] == color:
                dfs(nx,ny)

cnt1 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            cnt1 += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False]*n for _ in range(n)]

cnt2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            cnt2 += 1

print(cnt1, cnt2)
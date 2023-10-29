import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
land = dict()
landArr = []

number = 0
for i in range(n) :
    for j in range(m) :
        if data[i][j] == 1 and visited[i][j] == False :
            q = deque([(i, j)])
            visited[i][j] = True
            land[(i, j)] = number
            landArr.append((i, j, number))

            while q :
                x, y = q.popleft()
                for r, c in move :
                    nx = x + r
                    ny = y + c
                    if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == False and data[nx][ny] == 1 :
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        land[(nx, ny)] = number
                        landArr.append((nx, ny, number))
            number += 1

edges = []
for x, y, fromLand in landArr : # 좌표, 섬 번호
    for r, c in move :
        dist = 0
        nx = x + r
        ny = y + c
        while True :
            if not (0 <= nx < n and 0 <= ny < m) :
                break
            toLand = land.get((nx, ny))
            # 같은 번호의 섬일 경우
            if fromLand == toLand :
                break
            # 바다 위일 경우
            if toLand == None :
                nx = nx + r
                ny = ny + c
                dist += 1
                continue
            # 다리 길이가 2보다 작을 경우
            if dist < 2 :
                break

            edges.append((dist, fromLand, toLand)) # 섬과 섬 간의 거리
            break

edges = sorted(edges, reverse=True)
print(edges)

result = 0
count = number - 1
parents = [i for i in range(number)]
flag = 0

def find(k) :
    if k != parents[k] :
        parents[k] = find(parents[k])
    return parents[k]

def union(x, y) :
    x = find(x)
    y = find(y)
    parents[y] = x

# print(edges)
while count :
    try :
        distance, a, b = edges.pop() # 거리가 작은 것부터 pop
    except :
        flag = 1
        break

    if find(a) != find(b) :
        union(a, b)
        result += distance
        count -= 1

if flag == 1 :
    print(-1)
else :
    print(result)
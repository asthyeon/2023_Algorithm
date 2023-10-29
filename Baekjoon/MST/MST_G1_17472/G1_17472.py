import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 모든 섬을 연결하는 다리 길이 쵯소값 구하기
1. 모든 섬을 다리로 연결하려고 함
2. 색칠칸: 땅
3. 다리의 길이 = 다리가 격자에서 차지하는 칸의 수
4. 다리의 길이는 2 이상
5. 다리가 지나갈 때 옆으로 인접하는 섬은 연결 X
6. 다리는 교차 가능, 교차되는 중복된 부분도 다리 길이에 각각 포함
7. 모든 섬을 연결하는 것이 불가능하면 -1 출력
@ 풀이
(1) 섬마다 bfs로 고유번호 부여
(2) 각 가장자리에서 bfs로 다른 섬 탐색
(3) prim 알고리즘 사용
"""
import heapq


# 번호부여 bfs 함수
def numbering(sx, sy, number, arr, visited):
    q = [(sx, sy)]
    arr[sx][sy] = number
    visited[sx][sy] = number
    # 큐가 빌 때까지
    while q:
        x, y = q.pop()
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            # 벽 형성
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] != 0 and visited[nx][ny] == 0:
                arr[nx][ny] = number
                visited[nx][ny] = 1
                q.append((nx, ny))


# 각 섬과의 다리 길이를 재는 bfs 함수
def bfs(sx, sy, arr, distance):
    # 우방향
    x, y = sx, sy
    dist = 0
    while True:
        x, y = x, y + 1
        # 벽 형성
        if 0 <= x < N and 0 <= y < M:
            # 다음 구역이 바다면
            if arr[x][y] == 0:
                dist += 1
            # 다음 구역이 자기섬이면 종료
            elif arr[x][y] == arr[sx][sy]:
                break
            # 섬을 만나면 거리 리스트에 넣기
            else:
                # 거리가 1이라면 종료
                if dist == 1:
                    break
                distance[arr[sx][sy]].append((dist, arr[x][y]))
                distance[arr[x][y]].append((dist, arr[sx][sy]))
                break
        else:
            break
    # 하방향
    x, y = sx, sy
    dist = 0
    while True:
        x, y = x + 1, y
        # 벽 형성
        if 0 <= x < N and 0 <= y < M:
            # 다음 구역이 바다면
            if arr[x][y] == 0:
                dist += 1
            # 다음 구역이 자기섬이면 종료
            elif arr[x][y] == arr[sx][sy]:
                break
            # 섬을 만나면 거리 리스트에 넣기
            else:
                # 거리가 1이라면 종료
                if dist == 1:
                    break
                distance[arr[sx][sy]].append((dist, arr[x][y]))
                distance[arr[x][y]].append((dist, arr[sx][sy]))
                break
        else:
            break
    # 좌방향
    x, y = sx, sy
    dist = 0
    while True:
        x, y = x, y - 1
        # 벽 형성
        if 0 <= x < N and 0 <= y < M:
            # 다음 구역이 바다면
            if arr[x][y] == 0:
                dist += 1
            # 다음 구역이 자기섬이면 종료
            elif arr[x][y] == arr[sx][sy]:
                break
            # 섬을 만나면 거리 리스트에 넣기
            else:
                # 거리가 1이라면 종료
                if dist == 1:
                    break
                distance[arr[sx][sy]].append((dist, arr[x][y]))
                distance[arr[x][y]].append((dist, arr[sx][sy]))
                break
        else:
            break
    # 상방향
    x, y = sx, sy
    dist = 0
    while True:
        x, y = x - 1, y
        # 벽 형성
        if 0 <= x < N and 0 <= y < M:
            # 다음 구역이 바다면
            if arr[x][y] == 0:
                dist += 1
            # 다음 구역이 자기섬이면 종료
            elif arr[x][y] == arr[sx][sy]:
                break
            # 섬을 만나면 거리 리스트에 넣기
            else:
                # 거리가 1이라면 종료
                if dist == 1:
                    break
                distance[arr[sx][sy]].append((dist, arr[x][y]))
                distance[arr[x][y]].append((dist, arr[sx][sy]))
                break
        else:
            break


# prim 알고리즘
def prim(start, number, distances):
    pq = []
    MST = [0] * number
    # 시작점 인큐(시작거리, 시작섬)
    heapq.heappush(pq, (0, start))
    # 총 거리
    total = 0
    while pq:
        dist, now = heapq.heappop(pq)
        # 방문한 곳이라면 넘기기
        if MST[now] == 1:
            continue

        # 방문기록
        MST[now] = 1
        # 거리합산
        total += dist
        for new_dist, new in distances[now]:
            # 다음 지역이 방문하지 않은 곳이라면
            if MST[new] == 0:
                heapq.heappush(pq, (new_dist, new))

    # 모든 섬 연결 불가능시 -1 출력
    if sum(MST) != number - 1:
        return -1
    # 모든 섬 연결 가능시 총 거리 출력
    else:
        return total


# 지도 세로 N, 가로 M
N, M = map(int, input().split())
# 지도 입력
arr = [list(map(int, input().split())) for _ in range(N)]

# 방문행렬
visited = [[0] * M for _ in range(N)]
# 고유번호 부여
number = 1
for sx in range(N):
    for sy in range(M):
        if arr[sx][sy] == 1 and visited[sx][sy] == 0:
            numbering(sx, sy, number, arr, visited)
            number += 1

# 거리 리스트
distances = [[] for _ in range(number)]
# 다리 길이 재기
for sx in range(N):
    for sy in range(M):
        if arr[sx][sy] != 0:
            bfs(sx, sy, arr, distances)

# MST 확인
print(prim(1, number, distances))
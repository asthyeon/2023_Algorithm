import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 안전 거리가 가장 큰 칸 구하기
1. N x M 크기의 공간에 아기 상어 여러 마리
2. 1 x 1 크기의 정사각형 칸으로 나누어짐
3. 어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리
4. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수
5. 이동은 인접한 8방향(대각선 포함)이 가능
6. 0 은 빈 칸, 1 은 아기 상어 칸
@ 풀이
(1) 브루트포스로 풀어보기
(2) bfs
 - 다음 칸의 거리 값이 더 클 때만 이동하여 최소값 갱신하기
"""
from collections import deque


# bfs 함수
def bfs(q, arr, visited):
    # 큐가 빌 때까지
    while q:
        # 디큐
        x, y = q.popleft()

        # 델타탐색(8 방향)
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0], [-1, 1], [1, 1], [1, -1], [-1, -1]]:
            nx, ny = x + dx, y + dy

            # 벽 형성 및 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # 다음 칸이 빈 칸이거나 거리 값이 더 클 때만 이동
                if arr[nx][ny] == 0 or arr[nx][ny] > arr[x][y]:
                    visited[nx][ny] = 1
                    arr[nx][ny] = arr[x][y] + 1
                    q.append((nx, ny))

    # 가장 큰 안전거리 찾기
    result = 0
    for k in range(N):
        maximum = max(arr[k])
        if result < maximum:
            result = maximum

    return result - 1


# 가로 축의 수 N, 세로 축의 수 M
N, M = map(int, input().split())

# 공간의 상태 arr
arr = [list(map(int, input().split())) for _ in range(N)]

# 큐 생성
q = deque([])
# 방문리스트
visited = [[0] * M for _ in range(N)]

# 아기상어 위치 찾기
for i in range(N):
    for j in range(M):
        # 아기상어를 찾았다면 인큐 및 방문 기록
        if arr[i][j] == 1:
            q.append((i, j))
            visited[i][j] = 1

print(bfs(q, arr, visited))
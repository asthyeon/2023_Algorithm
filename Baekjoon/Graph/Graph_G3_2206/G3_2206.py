import sys
sys.stdin = open('input.txt')
from collections import deque

"""
# 최단 경로 찾기
1. 0: 이동가능 길, 1: 이동불가능 벽
2. 시작하는 칸과 끝나는 칸도 포함해서 세기
3. 한 개의 벽을 부수고 이동하는 것이 경로가 짧다면 벽을 한개까지 부수기
4. 불가능할 때는 -1 출력
5. 출발(1, 1), 도착(N, M)
@ 풀이
(1) bfs 사용
(2) 벽을 부수는 모든 경우를 고려하면 시간초과가 뜸
(3) 3차원 배열을 만들어 벽을 부순 경우와 부수지 않은 경우를 고려하기
"""


# bfs 함수
def bfs(sx, sy, arr, N, M):
    # 방문 리스트 생성
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    # 시작점 인큐
    q = deque([(sx, sy, 0)])
    # 시작점 방문 기록
    visited[sx][sy][0] = 1
    # 큐가 빌 때까지
    while q:
        # 디큐
        x, y, z = q.popleft()
        # 델타탐색
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            # 벽 형성
            if 0 <= nx < N and 0 <= ny < M:
                # 이동할 수 있는 통로일 때
                if arr[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    # 인큐
                    q.append((nx, ny, z))
                    # 방문 기록
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    # 도착점을 만나면 반복 종료
                    if nx == N - 1 and ny == M - 1:
                        q.clear()
                        break
            # 현재 위치가 벽이고, 벽을 아직 부수지 않았다면
                elif arr[nx][ny] == 1 and z == 0:
                    # 인큐
                    q.append((nx, ny, z + 1))
                    # 방문 기록
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1
                    # 도착점을 만나면 반복 종료
                    if nx == N - 1 and ny == M - 1:
                        q.clear()
                        break

    # 도착하지 못했을 때
    if visited[N - 1][M - 1][z] == 0:
        return 1000
    # 도착했을 때
    else:
        return visited[N - 1][M - 1][z]


# x좌표 N, y좌표 M
N, M = map(int, sys.stdin.readline().strip().split())

# 맵 받기
arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

# 최단 경로 카운트
cnt_min = 1000 * 1000

# 함수 사용
cnt = bfs(0, 0, arr, N, M)
if cnt_min > cnt:
    cnt_min = cnt

# 불가능할 때
if cnt_min == 1000:
    cnt_min = -1

print(cnt_min)

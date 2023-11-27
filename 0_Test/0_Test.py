import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 빙산
[출력: 빙산이 분리되는 최초의 시간 출력, 분리되지 않으면 0 출력]
1. 바다칸: 0
2. 빙산은 동서남북에 바다가 저장된 칸의 개수만큼 줄어듦(최대 0)
3. 한 덩어리의 빙산이 주어질 때 두 덩어리 이상으로 분리되는 최초의 시간 구하기
@ 풀이
(1) bfs로 분리 확인 및 빙산 녹이기
"""
from collections import deque

# 세로 N, 가로 M
N, M = map(int, input().split())
# 빙산 배열
arr = [list(map(int, input().split())) for _ in range(N)]

# 연수
year = 0
while True:
    # 복사본 만들기
    copied = [a[:] for a in arr]
    # 방문 기록
    visited = [[0] * M for _ in range(N)]
    # 덱 생성
    q = deque([])
    # 빙산유뮤 확인
    iceberg = False
    # 분리 여부
    parted = 0

    for x in range(N):
        for y in range(M):
            # 방문하지 않았다면 분리되어있는지 확인하기
            if visited[x][y] == 0 and arr[x][y] > 0:
                iceberg = True
                # 분리여부 체크(분리안된상태)
                if parted == 0:
                    parted = 1
                    # 시작점 인큐
                    q.append((x, y))
                    # 시작점 방문 기록
                    visited[x][y] = 1

                    while q:
                        sx, sy = q.popleft()

                        # 델타탐색
                        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                            nx, ny = sx + dx, sy + dy
                            # 벽형성
                            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                                # 빙산이라면 방문
                                if arr[nx][ny] > 0:
                                    visited[nx][ny] = 1
                                    q.append((nx, ny))
                # 분리되었다면 종료
                else:
                    print(year)
                    exit()

            # 빙산 녹이기
            if arr[x][y] > 0:
                melt = 0
                for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    nx, ny = x + dx, y + dy
                    # 벽형성(주변이 바다면 스택 추가
                    if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                        melt += 1

                copied[x][y] -= melt
                if copied[x][y] < 0:
                    copied[x][y] = 0

    # 원본 교체
    arr = [c for c in copied]
    # 빙산을 녹였다면 넘기기
    if iceberg:
        year += 1
        continue
    # 녹은 빙산이 없다면 종료
    else:
        print(0)
        exit()



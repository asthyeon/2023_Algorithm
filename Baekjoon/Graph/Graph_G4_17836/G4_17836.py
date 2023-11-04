import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 공주에게 도달 가능한 최단 시간 출력, 불가능시 Fail 출력
1. T 시간 후 공주 사망(T 시간에 공주를 만나도 구출 가능)
2. 그람 획득시 벽 부술 수 있음(개수 제한 X)
3. 1칸 이동시 1시간
@ 풀이
(1) 다익스트라 이용시 시간 초과 -> bfs
(2) 그람을 획득했을 때와 획득하지 않았을 때 구분하기
"""
from collections import deque


# 다익스트라 함수
def bfs(sx, sy):
    # 방문 리스트
    visited = [[0] * M for _ in range(N)]
    # 큐 생성 및 시작 위치 인큐
    q = deque([(sx, sy)])
    # 그람을 획득했을 때 목적지까지의 거리
    gram = 20000
    # 큐가 빌 때까지
    while q:
        x, y = q.popleft()
        # 델타 탐색
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            # 벽 형성 및 방문하지 않은 곳이라면
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                # 다음이 벽이면 넘기기
                if castle[nx][ny] == 1:
                    continue
                # 다음이 그람이면 획득한 후 목적지까지 거리 계산
                elif castle[nx][ny] == 2:
                    # 방문 처리
                    visited[nx][ny] = visited[x][y] + 1
                    # 목적지와의 거리
                    gram = (visited[nx][ny]) + ((N - 1) - nx) + ((M - 1) - ny)
                # 통로라면 시간 추가
                else:
                    # 방문 처리
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
                # 그람이 있다면 바로 거리값 계산 이동
            # 목적지에 도달했다면 바로 종료
            if visited[N - 1][M - 1] != 0:
                break

    # 목적지에 도달하지 못했다면 그람 리턴
    if visited[N - 1][M - 1] == 0:
        return gram
    # 목적지에 도달했다면 최소값 비교
    else:
        return min(visited[N - 1][M - 1], gram)


# 성 가로 N, 세로 M, 제한 시간 T
N, M, T = map(int, input().split())
# 성 지도(0: 통로, 1: 벽, 2: 그람)
castle = [list(map(int, input().split())) for _ in range(N)]

# 구출한다면 시간 출력, 실패한다면 Fail 출력
t = bfs(0, 0)
if t <= T:
    print(t)
else:
    print('Fail')
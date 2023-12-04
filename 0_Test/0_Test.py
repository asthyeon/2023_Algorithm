import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 상범 빌딩
[출력: 각 빌딩에 대해 답 출력(탈출시와 불가능시 출력문구)
1. 각 변의 길이가 1인 정육면체로 이루어짐
2. 금으로 이루어지면 지나갈 수 없고, 비어 있으면 지나갈 수 있음
3. 인접한 6개의 칸(동, 서, 남, 북, 상, 하)로 1분의 시간을 들여 이동 가능(대각선 불가능)
4. 출구를 통해서만 탈출 가능
5. 'S': 시작, 'E': 출구, '#': 금, '.': 비어 있음
@ 풀이
(1) bfs로 탈출시도
(2) 덱을 이용하여 가장 빠른 시간 찾기
"""
from collections import deque


# bfs 함수
def bfs(building, sf, sx, sy):
    # 방문 리스트
    visited = [[[0] * C for _ in range(R)] for _ in range(L)]
    # 큐 형성
    q = deque([])
    # 시간
    time = 0
    # 시작점 인큐
    q.append((time, sf, sx, sy))
    # 시작점 방문기록
    visited[sf][sx][sy] = 1
    # 큐가 빌 때까지
    while q:
        t, f, x, y = q.popleft()

        # 델타탐색
        t += 1
        for df, dx, dy in ((0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)):
            nf, nx, ny = f + df, x + dx, y + dy
            # 벽형성
            if 0 <= nf < L and 0 <= nx < R and 0 <= ny < C:
                # 비어있고 방문하지 않았다면 방문
                if building[nf][nx][ny] == '.' and visited[nf][nx][ny] == 0:
                    q.append((t, nf, nx, ny))
                    visited[nf][nx][ny] = 1
                # 도착지점이라면 종료
                elif building[nf][nx][ny] == 'E':
                    return f'Escaped in {t} minute(s).'

    # 탈출 못하는 경우
    return 'Trapped!'


# 여러 개의 테스트 케이스
while True:
    # 층 수 L, 행 수 R, 열 수 C
    L, R, C = map(int, input().split())
    # 전부 다 0 이면 종료
    if L == 0 and R == 0 and C == 0:
        break
    # 빌딩 정보
    building = []
    for _ in range(L):
        floor = []
        for _ in range(R + 1):
            line = list(input().rstrip())
            # 빈문자열은 생략하기
            if line == []:
                continue
            floor.append(line)
        building.append(floor)

    # 시작지점을 찾고 bfs 탐색시작
    started = False
    for sf in range(L):
        for sx in range(R):
            for sy in range(C):
                if building[sf][sx][sy] == 'S':
                    print(bfs(building, sf, sx, sy))
                    started = True
                    break
            if started:
                break
        if started:
            break
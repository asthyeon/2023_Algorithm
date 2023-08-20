import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 몇 마리의 지렁이가 필요한지
1. 배추땅: 1, 없는땅: 0
'''


# bfs 함수 생성
def bfs(N, M, sx, sy, arr):
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append((sx, sy))
    # 시작점 방문 표시
    arr[sx][sy] = 2
    # 큐가 빌 때까지
    while q:
        # 디큐
        x, y = q.pop(0)
        # 델타 탐색
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            # 벽 형성 및 배추 밭일 때
            if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] == 1:
                # 인큐
                q.append((nx, ny))
                # 방문 표시
                arr[nx][ny] = 2
    return True


T = int(input())
for tc in range(1, T + 1):
    # 가로길이 M, 세로길이 N, 배추의 위치의 개수 K
    M, N, K = map(int, input().split())
    # 배추밭 형성
    arr = [[0] * N for _ in range(M)]
    # 배추밭 연결
    for _ in range(K):
        v1, v2 = map(int, input().split())
        arr[v1][v2] = 1
    # 지렁이 수
    cnt = 0
    # 배추밭 탐색
    for sx in range(M):
        for sy in range(N):
            if arr[sx][sy] == 1:
                # 배추밭일 때 지렁이 수 + 1
                if bfs(N, M, sx, sy, arr):
                    cnt += 1

    print(cnt)
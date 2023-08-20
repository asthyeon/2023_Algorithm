import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 최소의 칸수 구하기
1. 시작점 (1, 1), 도착점 (N, M)
2. 칸을 셀 때 시작 위치와 도착 위치도 포함시키기
'''


# bfs 함수 생성
def bfs(sx, sy, maze):
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append((sx, sy))
    # 큐가 빌 때까지
    while q:
        # 디큐
        x, y = q.pop(0)
        # 델타 탐색
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = x + dx, y + dy
            # 벽 생성 및 통로(1)일 때
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                # 인큐
                q.append((nx, ny))
                # 방문 기록
                maze[nx][ny] = maze[x][y] + 1
    # 도착점 거리 출력
    return maze[N - 1][M - 1]


# N 개의 줄, M 개의 정수
N, M = map(int, input().split())

# 미로 형성
maze = [list(map(int, input().rstrip())) for _ in range(N)]

print(bfs(0, 0, maze))
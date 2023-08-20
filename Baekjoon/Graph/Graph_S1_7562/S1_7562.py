import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 각 테스트 케이스마다 나이트가 최소 몇 번만에 이동할 수 있는지 출력
1. 나이트 이동 칸 수 생각하기
'''


# bfs 함수 생성
def bfs(l, sx, sy, ex, ey, chess):
    # 큐 생성
    q = []
    # 시작점 인큐
    q.append((sx, sy))
    # 시작점 방문 기록
    chess[sx][sy] = 1
    # 델타 이동 리스트
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [2, 1, -1, -2, -2, -1, 1, 2]
    # 큐가 빌 때까지
    while q:
        x, y = q.pop(0)
        # 델타 탐색(나이트 이동 칸)
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            # 벽 생성 및 방문하지 않은 곳일 때
            if 0 <= nx < l and 0 <= ny < l and chess[nx][ny] == 0:
                # 인큐
                q.append((nx, ny))
                # 방문 기록
                chess[nx][ny] = chess[x][y] + 1
                # 도착점일 때 반복 종료
                if chess[nx][ny] == chess[ex][ey]:
                    break
    # 시작점 제외 거리 출력
    return chess[ex][ey] - 1


T = int(input())
for tc in range(1, T + 1):
    # 체스판 한 변의 길이
    l = int(input())
    # 체스 판 형성
    chess = [[0] * l for _ in range(l)]
    # 나이트 시작점
    sx, sy = map(int, input().split())
    # 나이트가 이동하려는 지점
    ex, ey = map(int, input().split())

    print(bfs(l, sx, sy, ex, ey, chess))
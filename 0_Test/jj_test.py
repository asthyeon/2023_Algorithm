import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque


def bfs():
    que = deque([(0, 0)])

    visited = [[-1] * N for _ in range(N)]

    visited[0][0] = arr[0][0]

    while que:
        i, j = que.popleft()

        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj

            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] < 0 or visited[ni][nj] > visited[i][j] + arr[ni][nj]:
                    que.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + arr[ni][nj]

    print('---')
    for i in range(N):
        print(visited[i])
    print('---')

    return visited[N - 1][N - 1]


tc = 0

while True:
    N = int(input())

    if not N:
        break

    tc += 1

    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'Problem {tc}: {bfs()}')
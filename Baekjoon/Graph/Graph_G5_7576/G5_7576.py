import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

'''
# 모든 토마토가 익는데 걸리는 시간
1. 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어있지 않은 칸
2. 처음부터 모든토마토가 익었으면 0 출력
3. 모두 익지못하는 상황 -1 출력
@ 풀이
(1) 토마토 위치를 전부 찾고 좌표 덱에 넣기
(2) 덱에 들어가 있는 좌표에서 델타탐색으로 bfs 실행
'''


# bfs 함수
def bfs(q, arr):
    global check
    # 큐가 비어있지 않다면
    if q:
        # 디큐
        sx, sy = q.popleft()
        # 델타탐색
        for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nx, ny = sx + dx, sy + dy
            # 벽 형성 및 이동할 수 있는 곳이라면
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 0:
                q.append((nx, ny))
                arr[nx][ny] = arr[sx][sy] + 1
        check += 1


# 상자 가로 칸: M, 상자 세로 칸: N
M, N = map(int, input().split())
# 토마토 배열 받기
arr = [list(map(int, input().split())) for _ in range(N)]
# 큐 형성
q = deque([])
# 익은 날짜
day = -1
# 토마토가 하나라도 익은게 있는지 없는지 확인하기 위한 변수
check = 0

# 토마토 찾기
for x in range(N):
    for y in range(M):
        if arr[x][y] == 1:
            q.append((x, y))

# bfs 탐색 시작
while q:
    bfs(q, arr)

# 토마토가 하나도 익지 않았다면
if check == 0:
    # 0 을 셀 변수
    zero = 0
    # 모든 토마토가 익어있는 경우 찾기
    for i in range(N):
        if day == 0:
            break
        for j in range(M):
            if arr[i][j] == 0:
                zero += 1
                break
    # 모두 익지 못하는 상황이라면
    if zero != N * M:
        day = -1
# 토마토가 하나라도 익었다면
else:
    for k in range(N):
        # 안 익은 토마토가 없다면
        if 0 not in arr[k]:
            if day < max(arr[k]) - 1:
                day = max(arr[k]) - 1
        # 안 익은 토마토가 있다면
        else:
            day = -1
            break

print(day)




import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 마법사 상어와 비바라기
[출력: M번의 이동이 모두 끝난 후 들어 있는 물의 양의 합 출력]
1. 비바라기 마법
2. N x N 격자의 각 칸에 바구니 존재, 바구니에 저장할 수 있는 물의 양에는 제한 X
3. 격자의 가장 왼쪽 윗 칸 (1, 1), 가장 오른쪽 아랫 칸 (N, N)
4. N번 행 아래에 1번 행이, 1번 행 위에는 N번 행 연결
5. N번 열 왼쪽에 1번 열이, 1번 열 오른쪽에는 N번 열 연결
6. 비바라기 시전시 (N, 1), (N, 2), (N-1, 1), (N-1, 2)에 비구름이 생김
7. 구름에 이동을 M번 명령하려고 함
8. i번째 이동 명령은 방향 d(i)와 거리S(i)로 이루어져 있음
9. 방향은 총 8개 순서대로 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
10. 이동 명령시 다음이 순서대로 진행
 - 모든 구름이 d(i) 방향으로 s(i)칸 이동
 - 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가함
 - 구름이 모두 사라짐
 - 물이 증가한 칸(r, c)에 물복사 버그 마법 시전
  - 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수 만큼(r, c)에 있는 바구니의 물의 양이 증가
  - 이 때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다
  - 예: (N, 2)에 인접한 대각선 칸 = (N - 1, 1), (N - 1, 3)
        (N, N)에 인접한 대각선 칸 = (N - 1, N - 1) 뿐
 - 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어듦
  - 이 때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 함
@ 풀이
(1) 순서에 따라서 구현해보기
(2) bfs 활용하기
[[0, 0, 1, 0, 2],
 [2, 3, 2, 1, 0],
 [4, 3, 2, 9, 0],
[1, 0, 3, 10, 0],
[8, 8, 3, 2, 0]]

[[0, 0, 1, 0, 2],
 [2, 3, 2, 1, 0],
 [4, 3, 2, 9, 0],
[1, 0, 7, 12, 0],
 [8, 8, 4, 3, 0]]

[[0, 0, 1, 0, 0],
 [0, 1, 0, 1, 0],
 [2, 1, 0, 7, 0],
[1, 0, 7, 12, 0],
 [6, 6, 4, 3, 0]]
"""
from collections import deque
# 방향 딕셔너리
directions = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1),
              5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}


# 구름 이동 함수
def cloud(arr, d, s, q, dq):

    while q:
        # 이동순서 및 좌표 디큐
        x, y = q.popleft()
        
        # 가로 d 방향으로 s 만큼 이동
        dx = directions[d][0] * s
        nx = x + dx
        # 세로 d 방향으로 s 만큼 이동
        dy = directions[d][1] * s
        ny = y + dy
        # 벽을 넘을 시 바꿔주기
        if nx < 0 or nx >= N:
            nx = (nx % N)
        if ny < 0 or ny >= N:
            ny = (ny % N)

        # 물 양 1 증가
        arr[nx][ny] += 1
        # 대각선 탐색을 위해 대각선 큐에 인큐
        dq.append((nx, ny))

    return


# 대각선 탐색 함수
def diagonal(arr, dq, visited):

    while dq:
        x, y = dq.popleft()
        # 증가할 물의 양
        water = 0
        for dx, dy in [(-1, 1), (1, 1), (1, -1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            # 벽 형성
            if 0 <= nx < N and 0 <= ny < N:
                # 대각선에 물이 있으면 증가
                if arr[nx][ny] > 0:
                    water += 1

        # 대각선에 물이 있는만큼 증가
        arr[x][y] += water
        # 방문 체크
        visited[x][y] = 1

    return


# 새 구름 탐색 함수
def find(arr, q, visited):

    for x in range(N):
        for y in range(N):
            # 방문했으면 구름 생성하지말고 넘기기
            if visited[x][y] == 1:
                visited[x][y] = 0
                continue
            # 물의 양이 2칸 이상이면 구름을 만들고 2 차감
            if arr[x][y] >= 2:
                q.append((x, y))
                arr[x][y] -= 2


# 격자 크기 N, 이동 수 M
N, M = map(int, input().split())
# 격자 정보
arr = [list(map(int, input().split())) for _ in range(N)]
# 큐 생성 및 이동 순서, 초기 비구름 좌표 인큐
q = deque([(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)])
# 대각선 큐
dq = deque([])
# 방문 행렬
visited = [[0] * N for _ in range(N)]
for _ in range(M):
    # 방향 d, 거리 s
    d, s = map(int, input().split())

    # 구름 이동
    cloud(arr, d, s, q, dq)
    # 대각선 탐색
    diagonal(arr, dq, visited)
    # 새 구름 탐색
    find(arr, q, visited)

    # print(arr)
    # print(q)

# 전체 물의 양 구하기
total = 0
for a in arr:
    total += sum(a)

print(total)











import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 다시 칠해야 하는 정사각형의 최소 개수 구하기
1. K x K 크기의 체스판으로 잘라낸 후에 몇 개의 정사각형을 칠하는지 구하기
2. 체스판은 검은색과 흰색이 번갈아서 칠해져 있어야함
3. 시작 칸은 검은색 or 흰색
@ 풀이
(1) 브루트포스가 아닌 다른 방법을 사용하기
(2) 2차원 배열 누적합 사용하기
누적합 = 해당 수의 왼쪽 + 해당 수의 위 + 해당 수 - 해당 수의 왼쪽 위
구간합 = 해당 수 - 해당 수의 왼쪽 - 해당 수의 오른쪽 + 해당 수의 왼쪽 위
"""

# x축 N, y축 M, 체스판 크기 K
N, M, K = map(int, input().split())

# 체스판
arr = [list(input().rstrip()) for _ in range(N)]

# 블랙으로 시작할 때 누적합
board_B = [[0] * (M + 1) for _ in range(N + 1)]
for x in range(1, N + 1):
    for y in range(1, M + 1):
        # 색이 다른경우 색칠 횟수 1
        if x % 2 == 0 and y % 2 == 0:
            if arr[x - 1][y - 1] != 'B':
                board_B[x][y] = 1
        elif x % 2 == 0 and y % 2 == 1:
            if arr[x - 1][y - 1] != 'W':
                board_B[x][y] = 1
        elif x % 2 == 1 and y % 2 == 0:
            if arr[x - 1][y - 1] != 'W':
                board_B[x][y] = 1
        else:
            if arr[x - 1][y - 1] != 'B':
                board_B[x][y] = 1
        # 누적합
        board_B[x][y] = (board_B[x][y - 1] + board_B[x - 1][y] + 
                         board_B[x][y] - board_B[x - 1][y - 1])

# 화이트로 시작할 때 누적합
board_W = [[0] * (M + 1) for _ in range(N + 1)]
for x in range(1, N + 1):
    for y in range(1, M + 1):
        # 색이 다른경우 색칠 횟수 1
        if x % 2 == 0 and y % 2 == 0:
            if arr[x - 1][y - 1] != 'W':
                board_W[x][y] = 1
        elif x % 2 == 0 and y % 2 == 1:
            if arr[x - 1][y - 1] != 'B':
                board_W[x][y] = 1
        elif x % 2 == 1 and y % 2 == 0:
            if arr[x - 1][y - 1] != 'B':
                board_W[x][y] = 1
        else:
            if arr[x - 1][y - 1] != 'W':
                board_W[x][y] = 1
        # 누적합
        board_W[x][y] = (board_W[x][y - 1] + board_W[x - 1][y]
                         + board_W[x][y] - board_W[x - 1][y - 1])

# K 값만큼 구간합 구하고 최소값 찾기
result = 2000 ** 2
for i in range(K, N + 1):
    for j in range(K, M + 1):
        # 각 판마다 구간합 구하기
        result_B = (board_B[i][j] + board_B[i - K][j - K]
                    - board_B[i - K][j] - board_B[i][j - K])
        result_W = (board_W[i][j] + board_W[i - K][j - K]
                    - board_W[i - K][j] - board_W[i][j - K])
        result2 = min(result_B, result_W)
        # 최소값 교체
        if result > result2:
            result = result2

print(result)
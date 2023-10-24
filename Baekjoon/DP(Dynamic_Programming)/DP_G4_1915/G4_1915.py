import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 가장 큰 정사각형 구하기
@ 풀이
(1) dp로 풀기
"""

# 세로길이 n, 가로길이 m
n, m = map(int, input().split())
# 행렬
arr = [list(map(int, input().rstrip())) for _ in range(n)]

# 최대 넓이
max_area = 0
# dp 행렬
dp = [[0] * m for _ in range(n)]

for x in range(n):
    for y in range(m):
        # 4칸의 사각형이 될 수 있을 때부터
        if x >= 1 and y >= 1:
            # 행렬의 값이 1이라면
            if arr[x][y] == 1:
                # 대각선 왼쪽 위, 위, 왼쪽이 1일 경우(사각형이 될 경우)
                if arr[x - 1][y - 1] == 1 and arr[x - 1][y] == 1 and arr[x][y - 1] == 1:
                    # 이전의 dp 값들 중 최소값 + 1
                    dp[x][y] = min(dp[x - 1][y - 1], dp[x - 1][y], dp[x][y - 1]) + 1
                    # 최대 넓이가 더 크다면 교체
                    if max_area < dp[x][y]:
                        max_area = dp[x][y]
                # 사각형이 안될 경우 dp 값 = 1
                else:
                    dp[x][y] = 1
        # 4칸의 사각형이 되기 전에
        else:
            # 행렬의 값이 1이라면
            if arr[x][y] == 1:
                # dp 값 1
                dp[x][y] = 1
                # 최대 넓이가 더 크다면 교체
                if max_area == 0:
                    max_area = 1

# 가로 x 세로 출력
print(max_area ** 2)
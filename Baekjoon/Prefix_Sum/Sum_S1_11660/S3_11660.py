import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# (x1, y1) ~ (x2, y2) 합 구하기
1. x1, y1 은 1부터 시작
2. (x1, y1) ~ (x2, y2)는 배열
@ 풀이
(1) 누적합 구하기
- 왼쪽과 위를 더한후 왼쪽위를 빼고 해당 수를 더한다
(2) (x1, y1) (x2, y2) 가 주어질 때 반복문이 아닌 단순 계산으로 풀기(시간 초과 고려)
"""

# 표의 크기 N, 합을 구해야 하는 횟수 M
N, M = map(int, input().split())

# 표 N x N
arr = [list(map(int, input().split())) for _ in range(N)]

# 누적합 구하기(인덱스 조정을 위해 N + 1)
pre_sum = [[0] * (N + 1) for _ in range(N + 1)]
for x in range(N):
    for y in range(N):
        # 처음 값
        if x == 0 and y == 0:
            pre_sum[x + 1][y + 1] = arr[x][y]
        # 그 외
        else:
            # 왼쪽 누적합 더하고 위 누적합 더하고 왼쪽 위 누적합 빼주고 해당 값 더하기
            pre_sum[x + 1][y + 1] = (pre_sum[x + 1][y] + pre_sum[x][y + 1] -
                                     pre_sum[x][y] + arr[x][y])

# 범위 받기
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    # 누적합 구하기(역순: 해당 수 - [x2][y1 - 1]값 - [x1 - 1][y2]값 + [x1 - 1][y1 - 1]값)
    result = (pre_sum[x2][y2] + pre_sum[x1 - 1][y1 - 1] -
              pre_sum[x2][y1 - 1] - pre_sum[x1 - 1][y2])

    print(result)


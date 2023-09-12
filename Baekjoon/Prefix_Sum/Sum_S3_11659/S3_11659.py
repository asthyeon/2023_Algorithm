import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 수 N 개중 i ~ j 번째 수까지의 합
"""

# 수 개수: N, 합을 구해야 하는 횟수: M
N, M = map(int, input().split())

# N 개의 수
N_list = list(map(int, input().split()))
N_list.insert(0, 0)

# 누적합
pre_sum = [0] * (N + 1)
for k in range(1, N + 1):
    pre_sum[k] = pre_sum[k - 1] + N_list[k]

# i ~ j 구간
for _ in range(M):
    i, j = map(int, input().split())

    result = pre_sum[j] - pre_sum[i - 1]

    print(result)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 각 사람이 돈을 인출하는데 필요한 시간의 최솟값 구하기
1. ATM 앞에 N 명의 줄
2. i 번 사람이 돈을 인출하는데 걸리는 시간 P분
@ 풀이
(1) 시간 순으로 정렬
"""

# 사람의 수 N
N = int(input())

# 각 사람이 돈을 인출하는데 걸리는 시간 P
P = list(map(int, input().split()))
P.sort()

# 누적합 구하기
prefix_sum = [0] * N
for i in range(N):
    if i == 0:
        prefix_sum[i] = P[0]
    else:
        prefix_sum[i] = prefix_sum[i - 1] + P[i]

print(sum(prefix_sum))
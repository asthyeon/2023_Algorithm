import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 연속적인 며칠 동안의 온도의 합이 가장 큰 값 계산하기
"""

# 온도를 측정한 전체 날짜 수: N, 합을 구하기 위한 연속적인 날짜 수: K
N, K = map(int, input().split())

# 온도 리스트
N_list = list(map(int, input().split()))
N_list.insert(0, 0)

# 누적합
pre_sum = [0] * (N + 1)
for i in range(1, N + 1):
    pre_sum[i] = pre_sum[i - 1] + N_list[i]

# K 값 만큼 날짜 수 중 최대 합 구하기
# 가장 작은값으로 최소값을 설정
result = min(pre_sum)
# K 만큼 시작해서
for j in range(K, N + 1):
    # K 번째 전의 값을 빼주기
    temp = pre_sum[j] - pre_sum[j - K]
    # 최대값 교체
    if result < temp:
        result = temp

print(result)
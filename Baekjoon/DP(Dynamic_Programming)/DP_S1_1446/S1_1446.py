import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 운전해야 하는 거리의 최솟값 출력
1. 고속도로를 지나며 지름길을 이용
2. 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없음
3. 지름길의 시작 위치는 도착 위치보다 작음
@ 풀이
(1) dp 이용
"""


# dp 함수
def dp(N, D, N_list):
    # 각 위치를 정상적으로 갔을 때 1씩 증가
    dp = [i for i in range(D + 1)]
    for j in range(D + 1):
        # 현재 위치가 이전 위치 + 1 과 지름길을 탔을 때의 경우와 비교 하여 작은 값으로 결정
        dp[j] = min(dp[j - 1] + 1, dp[j])
        # 지름길을 탈지 말지 결정하는 반복문
        for k in range(N):
            # 현재 위치가 지름길을 탈 수 있는 경우
            if j == N_list[k][0]:
                # 도착 지점이 고속도로 길이를 초과하지 않는다면
                if N_list[k][1] <= D:
                    # 도착 위치의 거리가 현재 계산되어 있는 값보다 지름길을 타서 가는 값이 더 작다면 교체
                    if dp[N_list[k][1]] > dp[j] + N_list[k][2]:
                        dp[N_list[k][1]] = dp[j] + N_list[k][2]
            # 현재 위치보다 지름길의 시작 위치가 더 커지면 반복 종료
            elif j < N_list[k][0]:
                break

    return dp[-1]


# 지름길의 개수 N, 고속도로의 길이 D
N, D = map(int, input().split())

# 지름길 리스트
N_list = []

# 현재 위치
current = 0

# 지름길의 시작 위치 s, 도착 위치 e, 길이 d
for _ in range(N):
    s, e, d = map(int, input().split())

    N_list.append((s, e, d))

# 지름길 시작 위치로 정렬
N_list.sort()

result = dp(N, D, N_list)

print(result)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 상자의 크기가 주어질 때 한 번에 넣을수 있는 최대의 상자 개수를 출력하기
1. 정육면체 상자가 일렬로 늘어서 있음
2. 앞에 있는 상자의 크기가 뒤에 있는 상자의 크기보다 작으면,
   앞에 있는 상자를 뒤에 있는 상자 안에 넣을 수 있음
@ 풀이
(1) dp 사용
"""


# dp 함수
def dynamic_programming(boxes):
    # dp 배열
    dp = [0] * n

    for i in range(n):
        # 첫번째는 무조건 1
        if i == 0:
            dp[i] = 1
            continue
        # 그 이후로 해당 값을 직전의 값들과 비교하여
        for j in range(i):
            # 해당 값이 이전의 값보다 크다면
            if boxes[i] > boxes[j]:
                # 이전 값 + 1과 갱신된 값중 큰 값으로 교체
                dp[i] = max(dp[j] + 1, dp[i])
            # 해당 값이 이전의 값보다 작거나 같다면 갱신된 값과 1 중 큰 값 부여
            else:
                dp[i] = max(1, dp[i])

    return max(dp)


# 상자의 개수 n
n = int(input())
# 각 상자들의 크기
boxes = list(map(int, input().split()))

print(dynamic_programming(boxes))




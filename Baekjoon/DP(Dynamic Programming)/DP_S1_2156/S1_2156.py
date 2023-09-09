import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 기장 많은 양의 포도주 마시기
1. 포도주 잔 선택시 모두 마시고 원래 위치 돌려놓기
2. 연속으로 놓여 있는 3잔 모두 마실 수 없음
@ 풀이
(1) dp로 풀기
(2) 계단 문제와 유사
(3) 경우의 수
[6]
[0, 6]
6
[6, 10]
[0, 6, 16]
16
[6, 10, 13]
[0, 6, 16, 23]
16 = 6 + 10
19 = 6 + 13
23 = 10 + 13
[6, 10, 13, 9]
[0, 6, 16, 23, 28]
25 = 6 + 10 + 9
28 = 6 + 13 + 9
23 = 10 + 13

"""


# dp 함수
def dp(n, wine):
    dp = [0] * (n + 1)
    dp[1] = wine[1]

    if n >= 2:
        dp[2] = dp[1] + wine[2]
    
    # n == 3 일 때, 3가지 경우의 수 존재
    if n >= 3:
        dp[3] = max(dp[2], wine[2] + wine[3], dp[1] + wine[3])

    if n >= 4:
        for i in range(4, n + 1):
            # 직전까지 마신 포도주 양 vs 2번째 전까지 + 현재 포도주 vs 3번째 전 + 직전 포도주 + 현재 포도주
            dp[i] = max(dp[i - 1], dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i])

    return dp[n]


# 포도주 잔 개수
n = int(input())

# 포도주의 양
wine = [0]
for _ in range(n):
    wine.append(int(input()))

print(dp(n, wine))


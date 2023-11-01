import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 모든 가짓수 % 15746 구하기
1. 01, 10은 만들 수 없음
2. 00, 1만 사용
@ 풀이
(1) dp 사용
    - dp[0] = 1
    - dp[1] = 1
    - dp[2] = 2: dp[1] + dp[0]
    - dp[3] = 3: dp[2] + dp[1]
    - dp[4] = 5: dp[3] + dp[2]
    - dp[5] = 8: dp[4] + dp[3]
    - 00001 10000 00100 00111 10011 11001 11100 11111
(2) 피보나치 수열
"""


# dp 함수
def dynamic_programming(N):
    dp = [0] * (N + 1)
    dp[0] = 1
    dp[1] = 1
    if N >= 2:
        for i in range(2, N + 1):
            dp[i] = (dp[i - 2] + dp[i - 1]) % 15746

    return dp[N]


# 자연수 N
N = int(input())

print(dynamic_programming(N))
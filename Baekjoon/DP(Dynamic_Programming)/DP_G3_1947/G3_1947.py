import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 경우의 수를 1,000,000,000으로 나눈 나머지 출력 
1. 대회에 참가한 모든 사람들은 선물을 하나 준비함
2. 대회가 끝난 후 각자 선물을 전달할 때 선물을 나누는 경우의 수 구하기
3. 모든 사람은 선물을 하나씩 받으며, 자기의 선물을 자기가 받는 경우는 없음
@ 풀이
(1) dp로 풀기
    - dp[1]: 0
    - dp[2]: 1  = dp[1] * 2 + 1
    - dp[3]: 2  = dp[2] * 3 - 1
    - dp[4]: 9  = dp[3] * 4 + 1 
    - dp[5]: 44 = dp[4] * 5 - 1
(2) 홀수일 때: (dp[i - 1] * i) - 1, 짝수일 때 (dp[i - 1] * i) + 1 
"""


# dp 함수
def dynamic_programming(N):
    dp = [0] * (N + 1)
    # 1명일 때는 0이므로 2명일 때부터 시작
    for i in range(2, N + 1):
        # 짝수일 때
        if i % 2 == 0:
            dp[i] = ((dp[i - 1] * i) + 1) % 1000000000
        # 홀수일 때
        else:
            dp[i] = ((dp[i - 1] * i) - 1) % 1000000000

    return dp[N]


# 대회에 참가한 학생 수 N
N = int(input())

print(dynamic_programming(N))
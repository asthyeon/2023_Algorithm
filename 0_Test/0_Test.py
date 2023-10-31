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
    - 1: 0
    - 2: 1
    - 3: 2
    - 4: 9
    - 5: 44
"""


# dp 함수
def dynamic_programming(N):
    dp = [0] * N
    dp[1] = 1
    dp[2] = 2
    for i in range(3, N):
        dp[i] = (dp[i - 1] * 5) - 1

    return dp[N - 1]


# 대회에 참가한 학생 수 N
N = int(input())

print(dynamic_programming(N))




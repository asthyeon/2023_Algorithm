import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 인가?
1. 1 <= N <= 100 (1~100)
2. 계단수: 인접한 모든 자리의 차이가 1인 수
3. 0으로 시작하는 수는 계단수 X
4. 정답을 1,000,000,000으로 나눈 나머지를 출력하기
@ 풀이
(1) DP로 풀기
"""


# dp 함수
def dp(N, start, end):
    dp = [0] * int(end)
    dp[10] = 9
    if N >= 2:
        for i in range(int(start), int(end)):
            dp[i] = dp[i - 1]
            if i == int(start):
                dp[i] = 0
            for j in range(N - 1):
                if int(str(i)[j]) == int(str(i)[j + 1]) + 1 or int(str(i)[j]) == int(str(i)[j + 1]) - 1:
                    if dp[i] == 0:
                        dp[i] = 1
                    else:
                        dp[i] += 1

    return dp[end]


# 자연수: N
N = int(input())

# 시작하는 자릿수 만들기
start = '1'
for _ in range(N):
    if N == 1:
        break
    start += '0'

# 마지막 자릿수 만들기
end = '1'
for _ in range(N):
    end += '0'

print(dp(N, start, end))
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
(2) 경우의 수(1씩 차이나므로 각 대각선에 해당)
1의 자리   0 1 2 3 4 5 6 7 8 9
개수       0 1 1 1 1 1 1 1 1 1
10의 자리  0 1 2 3 4 5 6 7 8 9
개수       1 1 2 2 2 2 2 2 2 1
100의 자리 0 1 2 3 4 5 6 7 8 9
개수       1 3 3 4 4 4 4 4 3 2
(3) dp[x][y] 2차원 배열로 x는 자리수, y는 1의자리 수로 넣어서 몇이 되는지 만들기
"""


# dp 함수
def dp(N):
    dp = [[0] * 10 for _ in range(101)]

    # N == 1
    for i in range(10):
        if i == 0:
            continue
        dp[1][i] = 1

    # N >= 2
    # 자리수 만큼 반복
    for x in range(2, N + 1):
        for y in range(10):
            # 0일 때는 0보다 1 큰 1만 받음
            if y == 0:
                dp[x][y] = dp[x - 1][y + 1]
            # 9일 때는 9보다 1 작은 8만 받음 
            elif y == 9:
                dp[x][y] = dp[x - 1][y - 1]
            # 나머지는 양쪽으로 받음
            else:
                dp[x][y] = dp[x - 1][y - 1] + dp[x - 1][y + 1]

    return sum(dp[N])


# 자연수: N
N = int(input())

print(dp(N) % 1000000000)
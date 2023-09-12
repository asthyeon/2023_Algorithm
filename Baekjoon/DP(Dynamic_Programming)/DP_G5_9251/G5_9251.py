import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 주어진 두 문자열의 LCS의 길이
1. LCS: 두 수열이 주어졌을 때 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제
@ 풀이
(1) 2차원 배열로 경우의 수 구하기
  y C A P C A K
x 0 0 0 0 0 0 0
A 0 0 1 1 1 1 1
C 0 1 1 1 2 2 2
A 0 1 2 2 2 3 3
Y 0 1 2 2 2 3 3
K 0 1 2 2 2 3 4
P 0 1 2 3 3 3 4
(2) 문자가 같을 때 [x-1][y-1] + 1
(3) 문자가 다를 떄 max([x-1][y], [x][y-1])
"""


# dp 함수
def dp(X, Y):
    dp = [[0] * (len(Y)) for _ in range(len(X))]
    
    for x in range(1, len(X)):
        for y in range(1, len(Y)):
            # 두 문자가 같다면 대각선 왼쪽 위의 수 + 1
            if X[x] == Y[y]:
                dp[x][y] = dp[x - 1][y - 1] + 1
            # 두 문자가 다르다면 왼쪽 값과 위쪽 값 중 큰 값으로 교체
            else:
                dp[x][y] = max([dp[x - 1][y], dp[x][y - 1]])

    # 최대값 구하기
    result = 0
    for i in range(len(X)):
        if result < max(dp[i]):
            result = max(dp[i])

    return result

# 두 문자열 X, Y
# 인덱스 조정
X = ' '
X += input().rstrip()
Y = ' '
Y += input().rstrip()

print(dp(X, Y))


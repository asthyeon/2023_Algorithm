import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 이친수
[출력: N자리 이친수의 개수 출력] 
1. 이친수
 - 이진수
 - 0으로 시작하지 않음
 - 1이 두 번 연속으로 나타나지 않음 
@ 풀이
(1) 직접 구해보기
N = 1 : 1 - 1개
N = 2 : 10 - 1개
N = 3 : 100, 101 - 2개
N = 4 : 1000, 1010, 1001 - 3개
N = 5 : 10000, 10100, 10010, 10001, 10101 - 5개
N = 6 : 100000, 101000, 100100, 100010, 100001, 101010, 101001, 100101 - 8개
(2) 피보나치 -> dp로 풀기
"""


# 피보나치 함수
def fibo(N):
    dp = [0] * N
    dp[0] = 1
    if N >= 2:
        dp[1] = 1
    if N >= 3:
        for i in range(2, N):
            dp[i] = dp[i - 2] + dp[i - 1]

    return dp[-1]


# N
N = int(input())

print(fibo(N))


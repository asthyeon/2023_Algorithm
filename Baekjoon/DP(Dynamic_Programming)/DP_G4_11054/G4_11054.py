import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 가장 긴 바이토닉 수열의 길이 구하기
1. 바이토닉 수열: 어떤 수 Sk를 기준으로 S1 < S2 < ... < S(k-1_ < Sk > S(k+1) > ... > S(N-1) > SN
@ 풀이
(1) 경우의 수(해당하는 수를 기준인 Sk로 보고 길이로 측정)
     [1]
길이  1
     [1, 5]
길이  1  2
     [1, 5, 2]
길이  1  3  2
     [1, 5, 2, 1]
길이  1  4  3  1
     [1, 5, 2, 1, 4]
길이  1  4  3  1  3
     [1, 5, 2, 1, 4, 3]
길이  1  4  3  1  4  3
     [1, 5, 2, 1, 4, 3, 4]
길이  1  4  3  1  4  3  4
     [1, 5, 2, 1, 4, 3, 4, 5]
길이  1  4  3  1  4  3  4  5
     [1, 5, 2, 1, 4, 3, 4, 5, 2]
길이  1  5  3  1  5  4  5  6  2
     [1, 5, 2, 1, 4, 3, 4, 5, 2, 1]
길이  1  6  3  1  6  5  6  7  3  1
(2) 증가하는 리스트와 감소하는 리스트 2개로 풀기
"""


# dp 함수
def dp(N, A, inc, dec):
    dp = [0] * (N + 1)

    # 증가하는 리스트
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            # 해당 수가 이전의 수 보다 크다면 이전의 수의 길이에 + 1 한 것과 비교해서 해당된 값 중 큰 값으로 교체
            if A[i] > A[j]:
                inc[i] = max(inc[i], inc[j] + 1)

    # 감소하는 리스트(인덱스를 역순으로 계산)
    for m in range(N, 0, -1):
        for n in range(m, N + 1):
            # 해당 수가 이전의 수 보다 크다면 이전의 수의 길이에 + 1 한 것과 비교해서 해당된 값 중 큰 값으로 교체
            if A[m] > A[n]:
                dec[m] = max(dec[m], dec[n] + 1)

    # 증가하는 리스트와 감소하는 리스트에 해당하는 인덱스 값을 서로 더하기
    for l in range(1, N + 1):
        # 중복 값 - 1
        dp[l] = inc[l] + dec[l] - 1

    return max(dp)


# 수열 A의 크기: N
N = int(input())

# 수열 A
A = list(map(int, input().split()))
# 인덱스 조정
A.insert(0, 0)

# 증가하는 리스트 기본 길이 1
inc = [1 for _ in range(N)]
inc.insert(0, 0)

# 감소하는 리스트 기본 길이 1
dec = [1 for _ in range(N)]
dec.insert(0, 0)

print(dp(N, A, inc, dec))
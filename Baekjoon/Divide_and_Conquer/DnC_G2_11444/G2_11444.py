import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# n이 주어졌을 때, n번째 피보나치 수를 1,000,000,007로 나눈 나머지 구하기
@ 풀이
(1) 분할 정복으로 풀기
(2) 행렬의 거듭제곱 형식으로 풀기
 - (F(n+1) Fn   ) = (1 1)^n
   (Fn     F(n-1) = (1 0)
"""


# 분할 정복 함수
def dnc(answer, n):
    if n == 1:
        return answer

    # 짝수일 때,
    elif n % 2 == 0:
        return even(dnc(answer, n // 2))
    # 홀수일 때, 자기 자신을 한 번 더 곱하기
    else:
        return odd(dnc(answer, n // 2), myself)


# 짝수 함수
def even(answer):
    # 제곱을 위한 행렬
    square = [i[:] for i in answer]
    for a in range(2):
        for b in range(2):
            num = 0
            for c in range(2):
                num += square[a][c] * square[c][b]
            answer[a][b] = num % 1000000007
    return answer


# 홀수 함수
def odd(answer, myself):
    # 제곱을 위한 행렬
    square = [i[:] for i in answer]
    for a in range(2):
        for b in range(2):
            num = 0
            for c in range(2):
                num += square[a][c] * square[c][b]
            answer[a][b] = num % 1000000007
    # 제곱을 위한 행렬
    square = [i[:] for i in answer]
    for a in range(2):
        for b in range(2):
            num = 0
            for c in range(2):
                num += square[a][c] * myself[c][b]
            answer[a][b] = num % 1000000007
    return answer


# n
n = int(input().rstrip())

# 정답 행렬
answer = [[1, 1], [1, 0]]

# 자기자신 행렬
myself = [[1, 1], [1, 0]]

dnc(answer, n)

print(answer[0][1])
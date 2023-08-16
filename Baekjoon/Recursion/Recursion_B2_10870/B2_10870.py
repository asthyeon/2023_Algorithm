import sys
sys.stdin = open('input.txt')

'''
# 재귀를 이용한 피보나치
'''

# 정수 N
N = int(input())

# 재귀함수
def fibo(N):
    if N > 1:
        N = fibo(N - 1) + fibo(N - 2)
    elif N == 1:
        N = 1
    else:
        N = 0

    return N

print(fibo(N))
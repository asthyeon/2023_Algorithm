import sys
sys.stdin = open('input.txt')

'''
# 재귀를 이용한 팩토리얼
'''

# 정수 N
N = int(input())

# 재귀함수
def recursion(N):
    if N > 1:
        N = N * recursion(N - 1)
    else:
        N = 1

    return N

print(recursion(N))
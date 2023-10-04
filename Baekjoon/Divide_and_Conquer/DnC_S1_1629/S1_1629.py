import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 자연수 A 를 B 번 곱한 수를 C 로 나눈 나머지 구하기
@ 풀이
(1) 분할 정복을 이용하기
"""


# 분할 함수
def divide(A, B, C):
    # 더이상 분할이 안된다면
    if B == 1:
        return A % C
    # 짝수일 때
    elif B % 2 == 0:
        return (divide(A, B // 2, C) ** 2) % C
    # 홀수일 때, 자기 자신을 한 번 더 곱해야함
    else:
        return ((divide(A, B // 2, C) ** 2) * A) % C


# A, B, C
A, B, C = map(int, input().split())

print(divide(A, B, C))

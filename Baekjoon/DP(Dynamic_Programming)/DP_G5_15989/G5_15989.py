import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 정수 n이 주어졌을 때 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램
1. 합을 나타낼 때는 수를 1개 이상 사용하기
2. 합을 이루고 있는 수의 순서만 다른 것은 같은 것으로 취급
@ 풀이
(1) dp 사용
 - n 을 2로 나눈 수(n // 2) + 1로만 이루어진 수(1개) 값을 더하기
 - n 에서 3 빼기
 - 반복 
"""


# dp 함수
def dynamic_programming(n):
    # 방법의 수
    cnt = 0
    while True:
        # 3일 때 경우의 수 3개
        if n == 3:
            cnt += 3
            break
        # 2일 때 경우의 수 2개
        elif n == 2:
            cnt += 2
            break
        # 1일 때 경우의 수 1개
        elif n == 1:
            cnt += 1
            break
        cnt += 1
        cnt += n // 2
        n -= 3

    return cnt


T = int(input())
for tc in range(1, T + 1):
    # 정수 n
    n = int(input())

    print(dynamic_programming(n))
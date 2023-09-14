import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 칠판에 쓰여 있는 문제가 주어졌을 때 결과 구하기
"""

# 양의 정수 A
A = int(input())

# 연산자
Operator = input().rstrip()

# 양의 정수 B
B = int(input())

if Operator == '+':
    result = A + B
else:
    result = A * B

print(result)
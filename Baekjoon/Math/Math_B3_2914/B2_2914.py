import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 저작권 멜로디의 평균값
1. 값 = (창영이 앨범에 수록된 곰에 포함되어 있는 저작권 멜로디 수) / (앨범 수록곡 수)
2. 평균값은 항상 올림을 해서 정수로 만듦
* 평균값에서 1을 빼고 전체 값에 1을 더하기
"""

# 수록곡 수 A, 평균값 I
A, I = map(int, input().split())

# 저작권
right = A * (I - 1) + 1

print(right)
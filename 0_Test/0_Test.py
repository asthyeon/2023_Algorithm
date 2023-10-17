import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 구간의 점수의 최댓값의 최솟값을 구하기
1. 구간은 다음과 같은 조건으로 나누기
 - 하나의 구간은 하나 이상의 연속된 수들로 이루어짐
 - 배열의 각 수는 모두 하나의 구간에 포함되어 있어야 함
 - 구간의 점수 = 구간에 속한 수의 최댓값과 최솟값의 차이
 - 배열을 M 개 이하의 구간으로 나누기
"""

# 배열의 크기 N, 구간을 나누는 기준 M
N, M = map(int, input().split())

# 배열
arr = list(map(int, input().split()))


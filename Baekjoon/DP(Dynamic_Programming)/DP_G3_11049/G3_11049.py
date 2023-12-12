import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 행렬 곱셈 순서
[출력: 주어진 행렬을 곱하는데 필요한 곱셈 연산의 최솟값 출력]
1. NxM 행렬 A와 MxK 행렬 B를 곱할 때 필요한 곱셈 연산의 수 = NxMxK
2. 행렬 N개를 곱하는 데 필요한 곱셈 연산의 수는 행렬을 곱하는 순서에 따라 달라지게 됨
@ 풀이
(1) dp로 풀기
(2) 연쇄 행렬 곱셈 알고리즘 사용
 - 어떤 순서로 곱셈을 할지 결정을 하는 것
 
"""

# 행렬의 개수 N
N = int(input())
# 각 행렬의 크기 입력 받기
arrays = []
for _ in range(N):
    arr = tuple(map(int, input().split()))

    arrays.append(arr)

print(arrays)
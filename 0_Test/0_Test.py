import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# k원이 되는 경우의 수 구하기
1. n 가지 종류의 동전 존재
2. 각각의 동전의 가치가 다름
3. 총 가치의 합이 k원이 되도록 하고 싶음
4. 각각의 동전은 몇 개라도 사용할 수 있음
@ 풀이
(1) dp 사용
 1. 1 10개 
 2. 1 8개  2
 2. 2 5개  
 3. 5 2개  
"""


# dp 함수
def dynamic_programming():
    pass


# 종류 가지 수 n 개, 총 가치의 합 k 원
n, k = map(int, input().split())
# 각각의 동전의 가치
values = []
for _ in range(n):
    value = int(input())
    values.append(value)


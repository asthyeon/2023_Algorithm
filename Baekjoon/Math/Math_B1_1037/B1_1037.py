import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# N의 진짜 약수들이 <모두> 주어질 때 N을 구하기
1. 양수 A가 N의 진짜 약수가 되려면
 - N이 A의 배수이고
 - A가 1과 N이 아니어야 한다
@ 풀이
(1) 진짜 약수들이 모두 주어지기 때문에
(2) 가장 작은 약수 x 가장 큰 약수 = N
"""

# N 의 진짜 약수의 개수
n = int(input())

# N 의 진짜 약수 A 리스트
A_list = list(map(int, input().split()))

result = min(A_list) * max(A_list)
print(result)

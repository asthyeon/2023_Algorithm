import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 집합인 set 이용
'''

# 집합 A의 원소 개수, 집합 B의 원소 개수
A, B = map(int, input().split())

# A 의 모든 원소
arr_A = set(map(int, input().split()))

# B 의 모든 원소
arr_B = set(map(int, input().split()))

# 대칭 차집합 구하기
A_minus_B = arr_A - arr_B
B_minus_A = arr_B - arr_A
result = len(A_minus_B) + len(B_minus_A)

print(result)

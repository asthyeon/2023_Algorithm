import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 분해합: N
N = int(input())

# 가장 작은 생성자 구하기
# 조합을 붙일 리스트 생성
combi = []

# # 카드 3장의 합 나열
# for A in arr:
#     for B in arr:
#         if B != A:
#             for C in arr:
#                 if C != A and C != B:
#                     combi.append(A + B + C)
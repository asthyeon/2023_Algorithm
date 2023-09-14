import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# N 개의 정수중에 M 개의 자연수 X가 존재하는지 알아내기
1. 존재하면 1 출력
2. 존재X 0 출력
@ 풀이
(1) 이진 탐색 사용
"""


# 이진 탐색 함수
def binary_search(X, N_list):
    start = 0
    end = N - 1
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if X == N_list[mid]:
            answer = 1
            break
        elif X > N_list[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    return print(answer)


# 자연수 N
N = int(input())
# N 개의 정수
N_list = list(map(int, input().split()))
# 오름차순 정렬
N_list.sort()
# 자연수 X 의 수
M = int(input())
M_list = list(map(int, input().split()))
for X in M_list:
    binary_search(X, N_list)
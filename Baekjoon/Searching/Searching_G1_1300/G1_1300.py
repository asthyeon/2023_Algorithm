import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# B 를 오름차순으로 정렬했을 때 B[k] 를 구해보자
1. 배열 A 의 크기: N x N
2. 배열에 들어있는 수 A[i][j] = i x j
3. 수 A[i][j] 를 일차원 배열 B 에 넣으면 B 의 크기는 N x N 이 된다
4. 배열 A 와 B 의 인덱스는 1 부터 시작
5. N 은 10^5 보다 작거나 같은 자연수
6. k 는 min(10^9, N^2)보다 작거나 같은 자연수
"""


# 이분 탐색 함수
def binary_search(N):
    start = 1
    end = N ** 2
    cnt = 0
    while start <= end:
        mid = (start + end) // 2


# 배열의 크기 N
N = int(input())

# B[k] 의 k
k = int(input())
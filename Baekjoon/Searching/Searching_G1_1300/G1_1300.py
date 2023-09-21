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
@ 풀이
(1) 이분탐색 사용
(2) N * N 배열에서 각 칸들의 값은 i * j 이므로 규칙 존재
 - 임의의 수 보다 작거나 같은 수의 개수를 구하는 식 존재
 - k 보다 작거나 같은 수는 k 를 각 행으로 나눈 몫. 다만 N 을 초과할 순 없음
(3) 이분탐색 사용법
 - 어떤 수를 정하고 그 수보다 작거나 같은 것이 몇 개인지 찾기
 - 그 개수가 k개라면 어떤 수는 k 번째 수가 됨
(4) 규칙을 찾는 것이 중요한 느낌
"""


# 이분 탐색 함수
def binary_search(N, k):
    start = 1
    end = N ** 2
    result = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0

        # mid 보다 작거나 같은 수의 개수 찾기
        for i in range(1, N + 1):
            # mid를 각 행으로 나눈 수와 N 중 작은 수를 더하기
            cnt += min(mid // i, N)

        # 작거나 같은 수의 개수가 k 보다 크거나 같으면 답을 갱신하고 범위 줄이기
        if cnt >= k:
            result = mid
            end = mid - 1
        # k 보다 작다면 범위를 넓히기
        else:
            start = mid + 1

    return result


# 배열의 크기 N
N = int(input())

# B[k] 의 k
k = int(input())

print(binary_search(N, k))
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열 구하기
@ 풀이
(1) 이분탐색으로 풀기
(2) 제일 긴 수열을 만들어 놓고 더 작은 값이 나오면 교체하면서 길이가 늘어나는지만 확인
"""


# 이분탐색 함수
def binary_search(answer, start, end, arr):
    result = 0
    while start <= end:
        mid = (start + end) // 2

        # 수열에 들어가 있는 값이 찾은 값보다 작다면 이후 범위 탐색
        if arr[mid] < answer:
            start = mid + 1
        # 크다면 결과 값을 mid 로 교체 후 이전 범위 탐색
        elif arr[mid] > answer:
            result = mid
            end = mid - 1
        # 수열에 들어가 있는 값이 같다면 반복 종료
        else:
            result = mid
            break

    return result


# 수열 A 의 크기 N
N = int(input())

# 수열 A
A = list(map(int, input().split()))

# 빈 리스트에 수를 하나씩 넣으며 이분탐색을 진행하여 수열 만들기
arr = []
for i in range(N):
    # 처음에는 바로 넣기
    if len(arr) == 0:
        arr.append(A[i])
    # 2번째부터
    else:
        # arr 의 마지막 수보다 수열의 수가 더 크다면 append
        if arr[-1] < A[i]:
            arr.append(A[i])
        # 더 작다면 이분 탐색후 나온 mid 인덱스에 해당하는 arr 수를 A[i]로 교체
        elif arr[-1] > A[i]:
            arr[binary_search(A[i], 0, len(arr) - 1, arr)] = A[i]

print(len(arr))

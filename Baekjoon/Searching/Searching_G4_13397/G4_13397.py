import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 배열과 M이 주어졌을 때 구간의 점수의 최댓값의 최솟값 구하기
1. 구간의점수: 구간에 속한 수의 최댓값과 최솟값의 차이
2. 하나의 구간은 하나 이상의 연속된 수들로 이루어짐
3. 배열의 각 수는 모두 하나의 구간에 포함되어야 함
@ 풀이
(1) 이분 탐색 사용
(2) 구간의 길이를 기준으로 찾기
"""


# 이분 탐색 함수
def binary_search(arr):
    start = 0
    end = max(arr)
    # 구간의 점수의 최대값의 최솟값
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        # 구간의 수
        section = 0
        # 구간의 시작점
        now = 0
        # 구간의 시작점 부터 반복문
        for i in range(1, N):
            score = max(arr[now:i + 1]) - min(arr[now:i + 1])
            # 구간의 점수가 이번 점수의 최대값보다 크다면
            if score > mid:
                # 구역을 하나 더하고 시작점을 끝점으로 교체
                section += 1
                now = i
        # 남은 구간을 구간 하나로 보고 더하기
        section += 1

        # 구간이 M 개 이하일 때 정답이 됨
        if section <= M:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1

    return answer


# 배열의 크기 N, 구간의 수 M 개 이하
N, M = map(int, input().split())

# 배열
arr = list(map(int, input().split()))

print(binary_search(arr))
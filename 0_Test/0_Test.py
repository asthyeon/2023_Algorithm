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
        now = 0
        for i in range(1, N):
            print(f'now:{now}, i:{i}')
            score = max(arr[now:i]) - min(arr[now:i])
            if score > mid:
                section += 1
                # print(f'now:{now}, i:{i}')
                now = i
        else:
            if now != N - 1:
                section += 1
            elif now == N - 1:
                section += 1

        if section <= M:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    print(f'start:{start}, end:{end}')

    return answer


# 배열의 크기 N, 구간의 수 M 개 이하
N, M = map(int, input().split())

# 배열
arr = list(map(int, input().split()))

print(binary_search(arr))
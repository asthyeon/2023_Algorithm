import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# C 개의 공유기를 N 개의 집에 적당히 설치 후 가장 인접한 두 공유기 사이의 거리를 최대로 구하기
1. 한 집에는 공유기 하나만 설치 가능
2. 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치
@ 풀이
(1) 이분 탐색으로 거리의 간격을 찾기
(2) mid를 거리의 간격으로 놓기
(3) 최대 거리를 찾아야 하므로 첫집과 마지막집은 무조건 선택
"""


# 이분탐색 함수
def binary_search(houses, N, C):
    # 시작점은 1(간격이 0이 될 수 없기 때문)
    start = 1
    # 끝점은 마지막집 위치에서 첫집의 위치를 빼주기
    end = houses[-1] - houses[0]
    result = 0
    while start <= end:
        # 설치될 거리의 간격
        mid = (start + end) // 2
        # 공유기가 설치된 집의 수(첫집은 무조건 설치)
        cnt = 1
        # 현재 공유기가 설치된 위치
        install = houses[0]

        # 공유기 설치(첫집은 생략)
        for i in range(1, N):
            # 다음 집이 현재 설치된 곳부터 간격만큼 떨어졌을 때
            if houses[i] >= install + mid:
                # 설치 추가 및 현재 설치된 위치 갱신
                cnt += 1
                install = houses[i]

        # 설치된 공유기가 설치할 수 있는 공유기보다 많거나 같다면 간격 늘리기
        if cnt >= C:
            start = mid + 1
            # C 만큼 설치된 상황에서의 최대 간격 교체
            result = mid
        # 설치된 공유기가 설치할 수 있는 공유기보다 적다면 간격 좁히기
        else:
            end = mid - 1

    return result


# 집 수 N, 공유기 수 C
N, C = map(int, input().split())

# 집들의 위치 받기
houses = []
for _ in range(N):
    loc = int(input())
    houses.append(loc)

# 이분탐색을 위한 정렬
houses.sort()

# 함수 사용
print(binary_search(houses, N, C))
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 냅색문제
[출력: 가방에 넣는 방법의 수 출력]
1. N 개의 물건을 가방에 넣는 방법의 수 구하기
2. 최대 C만큼의 무게를 넣을 수 있는 가방
3. 아무것도 안넣을 수도 있음
@ 풀이
(1) '중간에서 만나기' 알고리즘 사용
 - 맨 처음에 1회만 반으로 쪼개기
 - n^m 의 연산을 2n^(m/2) 으로 줄일 수 있음
(2) 전반부, 후반부로 반으로 나눈 후
(3) 각 부분에 나올 수 있는 조합을 구하기
(3) 후반부를 정렬하고 전반부를 반복하여 돌며 후반부를 탐색 
"""
from itertools import combinations


# 경우의 수 구하는 함수
def case(arr, cases):
    # 해당부의 모든 조합 구하기
    for i in range(len(arr) + 1):
        combi = combinations(arr, i)
        # 각 조합의 합을 해당부에 넣기
        for com in combi:
            cases.append(sum(com))

    return cases


# 이분탐색 함수
def binary_search(f, back_cases):
    global cnt
    start = 0
    end = len(back_cases) - 1
    while start <= end:
        # 기준 무게 찾기
        mid = (start + end) // 2
        # 무게를 넘어선다면 범위 줄이기
        if f + back_cases[mid] > C:
            end = mid - 1
        # 무게보다 작거나 같다면 범위 늘리기
        else:
            start = mid + 1
    # 기준 무게보다 작은 경우의 수 카운트
    cnt += start


# 물건의 수 N, 가방의 무게 C
N, C = map(int, input().split())
# 각 물건의 무게
things = list(map(int, input().split()))

# 중간에서 만나기
front = things[:N // 2]
back = things[N // 2:]

# 경우의 수 구하기
front_cases = []
back_cases = []
front_cases = case(front, front_cases)
back_cases = case(back, back_cases)

# 이분탐색에 쓸 후반부 정렬
back_cases.sort()

# 전반부 순회하여 후반부를 이분탐색
cnt = 0
for f in front_cases:
    # 해당 값이 이미 가방의 무게를 넘어선경우 넘기기
    if f > C:
        continue
    # 이분탐색, 해당 무게가 선택된 경우 그 무게보다 작은 경우의 수 카운트
    binary_search(f, back_cases)

print(cnt)

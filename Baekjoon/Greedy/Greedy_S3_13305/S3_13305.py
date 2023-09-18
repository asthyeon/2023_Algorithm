import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 제일 오른쪽 도시로 가는 최소 비용 출력
1. 처음 출발할 때 자동차에는 기름이 없어서 주유소에서 기름을 넣고 출발해야함
@ 풀이
(1) 다음 주유소가 더 저렴하다면 최소 충전
(2) 가장 저렴한 곳에서 만땅
"""

# 도시의 개수 N
N = int(input())
# 각 도로의 길이
length = list(map(int, input().split()))
# 각 주유소의 리터당 가격
price = list(map(int, input().split()))
# 현재 비용
expense = 0
# 현재 주유소 인덱스
idx = 0
for i in range(1, N):
    # 현재 주유소 가격이 i 번째 주유소 가격보다 더 크다면
    if price[idx] > price[i]:
        # 최소 주유만 하고 주유소 인덱스 교체
        expense += price[idx] * length[i - 1]
        idx = i
    # 현재 주유소 가격이 i 번째 주유소 가격보다 더 작다면 그대로
    else:
        expense += price[idx] * length[i - 1]

print(expense)
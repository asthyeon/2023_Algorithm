import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 이진 탐색 활용
1. 이진 탐색을 위해 사용할 리스트를 복제
2. 정렬하면 기존의 리스트의 인덱스 값이 파괴되므로
3. 복제한 리스트를 정렬하여 활용하기

# 이진 탐색 활용한 건 시간 초과 나므로 다른 방법 사용
1. 빈 딕셔너리를 만들고
2. 빈 딕셔너리에 각 카드 숫자와 카운트 수를 키, 값으로 배정
3. 확인할 숫자가 있으면 카운트 수 출력
'''

# 상근이의 카드 수 N
N = int(input())

# 숫자 카드에 적혀 있는 정수
cards = list(map(int, input().split()))

# 맞춰야할 카드 수 M
M = int(input())

# 맞춰야할 카드 목록
checks = list(map(int, input().split()))

# # 리스트 복제하기
# checks_list = checks.copy()

# # 복제 리스트 정렬
# checks_list.sort()

# # 빈 리스트 생성
# arr = [0] * M

# # 카드들 반복
# for card in cards:
#     # 이진 탐색
#     start = 0
#     end = M - 1
#     while start <= end:
#         middle = (start + end) // 2
#         if checks_list[middle] == card:
#             arr[checks.index(checks_list[middle])] += 1
#             break
#         elif checks_list[middle] > card:
#             end = middle - 1
#         else:
#             start = middle + 1

# print(*arr)

# 딕셔너리 이용하기
card_dict = {}

# 빈 딕셔너리에 각 카드를 넣고, 없으면 1로 형성, 있으면 +1 하기
for card in cards:
    if card in card_dict:
        card_dict[card] += 1
    else:
        card_dict[card] = 1

# 숫자가 카운트 된 딕셔너리에 확인할 숫자가 있으면 출력, 없으면 0 출력
for check in checks:
    if check in card_dict:
        print(card_dict[check], end = " ")
    else:
        print(0, end = " ")
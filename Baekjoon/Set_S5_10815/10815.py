import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 상근이의 카드 개수
N = int(input())
# 숫자 카드에 적혀있는 정수
n_list = list(map(int, input().split()))
# 확인해야할 숫자 카드 개수
M = int(input())
# 확인해야할 숫자 카드의 정수
m_list = list(map(int, input().split()))

'''
# 이중 포문으로는 시간 초과이므로 이진탐색을 사용하기
1. 확인할 리스트를 정렬하기
2. 이진탐색 실행
'''

# 확인할 리스트 정렬
n_list.sort()

# 이진탐색 실행
for i in m_list:
    start = 0
    end = N - 1
    result = 0
    while start <= end:
        middle = (start + end) // 2
        if n_list[middle] == i:
            result = 1
            break
        elif n_list[middle] > i:
            end = middle - 1
        else:
            start = middle + 1
    print(result, end = ' ')
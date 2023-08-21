import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 좌표 압축 적용하기
1. Xi를 좌표 압축한 결과 Xi 의 값은 Xi > Xj 를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.
2. 시간초과를 피할 딕셔너리를 만들기
'''

N = int(input())
numbers = list(map(int, input().split()))

# 순서 정렬
numbers_sort = list(sorted(set(numbers)))

# 딕셔너리 생성
numbers_dict = {}

# 인덱스 값으로 작은 수 넣기
idx = -1
for number_sort in numbers_sort:
    idx += 1
    numbers_dict[number_sort] = idx

# 딕셔너리 출력
for number in numbers:
    print(numbers_dict[number], end=' ')


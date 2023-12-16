import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 최솟값과 최댓값
[출력: 첫째 줄부터 K줄에 걸쳐 구간의 합 출력] 
1. 어떤 N 개의 수가 주어져 있음(순서대로)
2. 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려고 함
@ 풀이
(1) 세그먼트 트리 이용
"""


# 트리 값 입력 함수
def init(start, end, index):
    # 가장 끝에 도달하면 값 반환
    if start == end:
        tree[index] = integers[start]
        return tree[index]
    # 도달하지 않았다면 좌우 나누며 재귀
    mid = (start + end) // 2
    left = init(start, mid, index * 2)
    right = init(mid + 1, end, (index * 2) + 1)
    # 좌측 노드와 우측 노드를 채우며 부모 노드의 값도 채우기
    tree[index] = left + right
    return tree[index]


# 구간 합 구하는 함수(first ~ last 까지의 합)
def prefix_sum(start, end, index, first, last):
    # 범위 밖에 있는 경우 기본값 반환
    if first > end or last < start:
        return 0
    # 범위 안에 있는 경우 값 반환
    if first <= start and last >= end:
        return tree[index]
    # 그렇지 않다면 두 부분으로 나누어 합 구하기
    mid = (start + end) // 2
    left = prefix_sum(start, mid, index * 2, first, last)
    right = prefix_sum(mid + 1, end, (index * 2) + 1, first, last)
    return left + right


# 수를 수정하는 함수
def modify(start, end, index, target, modified):
    # 수정할 수가 범위 밖에 있는 경우 끝내기
    if target < start or target > end:
        return
    # 범위 안에 있으면 그 지점까지 갱신
    tree[index] += modified
    if start == end:
        return
    mid = (start + end) // 2
    # 왼쪽 자식 및 오른쪽 자식 수정
    modify(start, mid, index * 2, target, modified)
    modify(mid + 1, end, (index * 2) + 1, target, modified)


# 트리 생성
tree = [0] * ((1500 ** 2) * 2)

# 수의 개수 N, 변경 횟수 M, 구간의 합 구하는 횟수 K
N, M, K = map(int, input().split())
# N개의 수
integers = []
for _ in range(N):
    integer = int(input())
    integers.append(integer)

# 트리에 값 입력
init(0, N - 1, 1)

# a가 1인 경우 b번째 수를 c로 바꾸기
# a가 2인 경우 b번째 수부터 c번째 수까지의 합을 구하여 출력
for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        # c 에서 b만큼 값을 뺀 값으로 바꾸기
        modified = c - integers[b - 1]
        # 정수 리스트 수정하기
        integers[b - 1] = c
        # 바뀐 수를 이용해 수정
        modify(0, N - 1, 1, b - 1, modified)

    else:
        # 구간 합 출력
        print(prefix_sum(0, N - 1, 1, b - 1, c - 1))


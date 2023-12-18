import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 커피숍2
[출력: 한 턴마다 구한 합을 한 줄마다 한 개씩 출력]
1. N개의 정수가 있으면 구간합을 구하거나 수를 수정해야하는 경우가 있음
2. 구간합과 수정을 할 수 있는 기능 필요
3. x, y는 x ~ y까지의 합(x > y 인 경우 y ~ x)
4. a, b는 a번째 수를 b로 바꾸기
@ 풀이
(1) 세그먼트 트리 이용
"""


# 트리 값 입력 함수
def init(start, end, index):
    # 끝까지 도달하면 값 입력 및 반환
    if start == end:
        tree[index] = integers[start]
        return tree[index]
    # 도달하지 않았다면 좌우 나누며 자식 노드로 재귀
    mid = (start + end) // 2
    left = init(start, mid, index * 2)
    right = init(mid + 1, end, (index * 2) + 1)
    # 자식 노드들을 채우며 부모 노드의 값도 채우기
    tree[index] = left + right
    return tree[index]


# 구간 합 구하는 함수(first ~ last)
def prefix_sum(start, end, index, first, last):
    # 구간이 범위를 벗어나면 기본값 반환
    if first > end or last < start:
        return 0
    # 구간이 시작값보다 작거나 같고 마지막값보다 크거나 같으면 구간 값 리턴
    if first <= start and last >= end:
        return tree[index]
    # 그렇지 않다면 좌우 나누며 자식 노드로 재귀 후 합 구하기
    mid = (start + end) // 2
    left = prefix_sum(start, mid, index * 2, first, last)
    right = prefix_sum(mid + 1, end, (index * 2) + 1, first, last)
    return left + right


# 값 수정 함수
def modify(start, end, index, target, modified):
    # 수정할 수가 범위 밖에 있는 경우 종료
    if target < start or target > end:
        return
    # 범위 안에 있으면 변경된 값만큼 더하기
    tree[index] += modified
    # 리프 노드라면 종료
    if start == end:
        return
    # 자식 노드라면 좌우 나누며 재귀
    mid = (start + end) // 2
    modify(start, mid, index * 2, target, modified)
    modify(mid + 1, end, (index * 2) + 1, target, modified)


# 수의 개수 N, 턴의 개수 Q
N, Q = map(int, input().split())
# 처음 배열에 들어가 있는 정수 N개
integers = list(map(int, input().split()))

# 트리 생성
tree = [0] * (N * 4)
# 트리 값 입력
init(0, N - 1, 1)

# 턴
for _ in range(Q):
    # x ~ y의 합을 구하고, a번째 수를 b로 바꾸기
    x, y, a, b = map(int, input().split())

    # 구간 합 출력(x, y 크기 비교)
    if x > y:
        print(prefix_sum(0, N - 1, 1, y - 1, x - 1))
    else:
        print(prefix_sum(0, N - 1, 1, x - 1, y - 1))

    # 값 수정하기
    # a번째 수에서 b만큼 값을 뺀 값으로 바꾸기
    modified = b - integers[a - 1]
    # 정수 리스트 수정하기
    integers[a - 1] = b
    # 수정
    modify(0, N - 1, 1, a - 1, modified)
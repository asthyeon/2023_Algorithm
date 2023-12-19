import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 최솟값과 최댓값
[출력: M개의 줄에 입력받은 순서대로 각 a, b에 대한 답을 최솟값, 최댓값 순서로 출력]
1. a번째 정수부터 b번째 정수 중 제일 작은 정수, 큰 정수 찾기
2. a, b 쌍이 M개 주어짐
3. 입력된 순서대로 a ~ b 번 정수 중 최소, 최댓값 찾기
@ 풀이
(1) 세그먼트 트리 이용
 - 여러 개의 데이터가 존재할 때 특정 구간의 결과값을 구하는데 사용
 - 이진 트리의 형태
 - 선형 탐색보다 효율적
 - 시간복잡도: O(logN)
 - 단점으로는 완탐에 비해 더 많은 메모리가 필요
"""


# 최댓값 트리 생성 함수
def max_init(start, end, index):
    # 가장 끝에 도달했으면 값 배정
    if start == end:
        max_tree[index] = integers[start]
        return max_tree[index]
    # 도달하지 않았다면 좌우 나누기
    mid = (start + end) // 2
    left = max_init(start, mid, index * 2)
    right = max_init(mid + 1, end, (index * 2) + 1)
    # 좌측 노드와 우측 노드를 채워주면서 부모 노드의 값도 채우기
    max_tree[index] = max(left, right)
    return max_tree[index]


# 최솟값 트리 생성 함수
def min_init(start, end, index):
    # 가장 끝에 도달했으면 값 배정
    if start == end:
        min_tree[index] = integers[start]
        return min_tree[index]
    # 도달하지 않았다면 좌우 나누기
    mid = (start + end) // 2
    left = min_init(start, mid, index * 2)
    right = min_init(mid + 1, end, (index * 2) + 1)
    # 좌측 노드와 우측 노드를 채워주면서 부모 노드의 값도 채우기
    min_tree[index] = min(left, right)
    return min_tree[index]


# 최댓값 구하는 함수
def maximum(start, end, index, left, right):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return 0
    # 범위 안에 있는 경우
    if left <= start and right >= end:
        return max_tree[index]
    # 그렇지 않다면 두 부분으로 나누기
    mid = (start + end) // 2
    # start와 end가 변하면서 최댓값 찾기
    return max(maximum(start, mid, index * 2, left, right), maximum(mid + 1, end, (index * 2) + 1, left, right))


# 최솟값 구하는 함수
def minimum(start, end, index, left, right):
    # 범위 밖에 있는 경우
    if left > end or right < start:
        return 10e10
    # 범위 안에 있는 경우
    if left <= start and right >= end:
        return min_tree[index]
    # 그렇지 않다면 두 부분으로 나누기
    mid = (start + end) // 2
    # start와 end가 변하면서 최댓값 찾기
    return min(minimum(start, mid, index * 2, left, right), minimum(mid + 1, end, (index * 2) + 1, left, right))


# 정수 개수 N, a, b의 쌍 수 M
N, M = map(int, input().split())
# N 개의 정수
integers = []
for _ in range(N):
    integer = int(input())
    integers.append(integer)

# 트리 생성(배열의 개수가 N개일 때, N보다 큰 가장 가까운 N의 제곱수를 구한 뒤에 그것의 2배)
# 넉넉하게 만들기
max_tree = [0] * ((400 ** 2) * 2)
min_tree = [10e10] * ((400 ** 2) * 2)

# 트리에 값 부여
max_init(0, N - 1, 1)
min_init(0, N - 1, 1)
print(min_tree[:40])

# M 개의 a, b 쌍마다 구하기
for _ in range(M):
    a, b = map(int, input().split())

    ans_min = minimum(0, N - 1, 1, a - 1, b - 1)
    ans_max = maximum(0, N - 1, 1, a - 1, b - 1)
    print(ans_min, ans_max)
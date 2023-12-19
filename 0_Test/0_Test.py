import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 수열과 쿼리 15
1. 길이가 N인 수열
2. 다음 쿼리 수행
 - 1 i v : A[i]를 v로 바꾸기
 - 2 : 수열에서 크기가 가장 작은 값의 인덱스를 출력
 - 2의 경우가 여러 개인 경우 인덱스가 작은 것을 출력
3. 수열의 인덱스는 1부터 시작
@ 풀이
(1) 세그먼트 트리 이용
(2) 인덱스를 구해야 하므로 인덱스 값도 함께 저장해서 구하기
"""


# 트리 값 입력 함수
def init(start, end, index):
    # 가장 끝까지 도달하면 인덱스와 값 부여
    if start == end:
        tree[index] = [start, A[start]]
        return tree[index]
    # 도달하지 않았으면 좌우 나누고 자식 노드로 재귀
    mid = (start + end) // 2
    left = init(start, mid, index * 2)
    right = init(mid + 1, end, (index * 2) + 1)
    # 자식 노드의 값을 채우며 부모 노드의 값도 채우기
    # 자식 노드들중 더 작은 값을 찾고 부여하기
    if left[1] > right[1]:
        tree[index] = [right[0], right[1]]
    else:
        tree[index] = [left[0], left[1]]
    return tree[index]


# 트리 최소값 찾는 함수
def min_value(start, end, index, first, last):
    # 구간이 범위를 벗어나면 기본 값 반환
    if first > end or last < start:
        return 10e9

    # 구간이 수열의 크기보다 크다면 구간 값 반환
    if first <= start and last >= end:
        return tree[index]
    
    # 그렇지 않다면 좌우로 나누고 자식 노드로 재귀
    mid = (start + end) // 2
    left = min_value(start, mid, index * 2, first, last)
    right = min_value(mid + 1, end, (index * 2) + 1, first, last)
    # 자식 노드들중 더 작은 값을 찾고 리턴
    if left[1] > right[1]:
        return [right[0], right[1]]
    else:
        return [left[0], left[1]]


# 트리 값 수정 함수
def modify(start, end, index, target, modified):
    # 수정할 값이 범위를 벗어나면 종료
    if target < start or target > end:
        return
    # 리프노드라면 값 수정
    if start == end:
        tree[index] = [start, modified]
        return
    # 리프 노드가 아니라면 좌우 나누며 자식 노드로 재귀
    mid = (start + end) // 2
    modify(start, mid, index * 2, target, modified)
    modify(mid + 1, end, (index * 2) + 1, target, modified)

    # 더 작은 값으로 부모 노드 값 수정
    if tree[index * 2][1] > tree[(index * 2) + 1][1]:
        tree[index] = [tree[(index * 2) + 1][0], tree[(index * 2) + 1][1]]
    else:
        tree[index] = [tree[index * 2][0], tree[index * 2][1]]


# 수열의 크기 N
N = int(input())
# 수열
A = list(map(int, input().split()))
# 쿼리의 개수 M
M = int(input())

# 트리 생성
tree = [10e9] * (N * 4)
# 트리 값 입력
init(0, N - 1, 1)

# print(f'A: {A}')
# print(f'tree: {tree[:N + 1]}')

# 쿼리 수행
for _ in range(M):
    query = input().rstrip()

    # 쿼리가 2일 때 수행
    if query == '2':
        index, value = min_value(0, N - 1, 1, 0, N - 1)
        print(index + 1)

    # 쿼리가 1일 때 수행
    else:
        # 쿼리를 나누기
        query, i, v = query.split(' ')
        # 수열값 수정
        A[int(i) - 1] = int(v)
        # 수정
        modify(0, N - 1, 1, int(i) - 1, int(v))
        # print(f'A: {A}')
        # print(f'tree: {tree[:N + 1]}')
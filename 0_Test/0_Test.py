import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 가계부 (Hard)
1. 가계부 프로그램 만들기
 - 월곡이의 생후 p일에 수입/지출 내용 추가하기(수입: 양수, 지출: 음수)
 - 월곡이의 생후 p일부터 q일까지 잔고가 변화한 값을 구하고 출력
  (월곡이가 빚을 졌다면 어떤 i에 대해서 생후 i일의 잔고는 음수일 수 있음)
* 입력
- 첫째 줄: 월곡이가 살아온 날 N, 쿼리의 개수 Q
- 둘째 줄 ~ Q+1번째 줄
 - 1 p x: 생후 p일에 x를 추가
 - 2 p q: 생후 p일부터 q일까지 변화한 양 출력
[출력: 각 2 쿼리에 대해 계산된 값 출력]
"""

"""
@ 풀이
(1) 세그먼트 트리 이용하기
(2) init을 통해서 값을 추가하고 변화한 양은 구간 합이라고 생각하기
(3) 기본 값이 없기 때문에 init이 아닌 add 함수를 만들기(기존의 modify 함수)
"""


# 트리 값 추가 함수
def add(start, end, index, target, added):
    # 추가될 값이 범위를 벗어나면 종료
    if target < start or target > end:
        return

    # 범위 안에 있으면 값 할당
    tree[index] += added

    # 리프 노드가 되었다면 종료
    if start == end:
        return

    # 리프 노드가 아니라면 좌우 나누며 자식 노드로 재귀
    mid = (start + end) // 2
    add(start, mid, index * 2, target, added)
    add(mid + 1, end, (index * 2) + 1, target, added)


# 트리 값 구간 구하기
def prefix_sum(start, end, index, first, last):
    # 구간이 범위를 벗어나면 기본 값 반환
    if first > end or last < start:
        return 0

    # 구간이 범위보다 크다면 구간 값 반환
    if first <= start and last >= end:
        return tree[index]

    # 그렇지 않다면 좌우로 나누고 자식 노드로 재귀
    mid = (start + end) // 2
    left = prefix_sum(start, mid, index * 2, first, last)
    right = prefix_sum(mid + 1, end, (index * 2) + 1, first, last)
    # 구간 합 반환
    return left + right


# 월곡이가 살아온 날 N, 쿼리 개수 Q
N, Q = map(int, input().split())

# 트리 생성
tree = [0] * (N * 4)

# 쿼리 수행
for _ in range(Q):
    query, p, q = map(int, input().split())
    
    # 생후 p일에 q를 추가
    if query == 1:
        # 트리 값 추가
        add(0, N - 1, 1, p - 1, q)
    
    # 생후 p일부터 q일까지 변화된 양 출력
    else:
        print(prefix_sum(0, N - 1, 1, p - 1, q - 1))

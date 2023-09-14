import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

"""
# 최소 힙으로 입력에서 0이 주어진 횟수만큼 답 출력
1. 연산
- 배열에 자연수 X 넣기
- 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거
2. 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한다면 0 출력
@ 풀이
(1) 최소 힙 구현하기
"""


# 최소 힙 함수
def min_heap(heap, heap_idx):
    # 부모노드가 자식노드보다 크다면 교체
    if heap[heap_idx // 2] > heap[heap_idx]:
        heap[heap_idx // 2], heap[heap_idx] = heap[heap_idx], heap[heap_idx // 2]
        # 부모 위치에서 다시 힙 함수 적용
        min_heap(heap, heap_idx // 2)
    # 부모노드가 자식노드보다 같거나 작다면 종료
    else:
        return


# 힙 삭제 함수
def heap_sort(heap):
    global heap_idx
    # 루트노드 저장
    result = heap[1]
    # 힙의 루트노드를 마지막 노드로 교체
    heap[1] = heap.pop()
    # 힙 인덱스 -1
    heap_idx -= 1
    # 부모 인덱스
    p = 1
    # 왼쪽 자식 인덱스
    c = p * 2
    # 자식이 하나라도 있으면
    while c <= heap_idx:
        # 오른쪽 자식이 있고, 오른쪽 자식이 더 작으면
        if c + 1 <= heap_idx and heap[c] > heap[c + 1]:
            # 오른쪽 자식과 비교하기
            c += 1
        # 자식 노드가 부모노드보다 더 작다면
        if heap[p] > heap[c]:
            # 부모 노드와 자식 노드 교체
            heap[p], heap[c] = heap[c], heap[p]
            # 자식 노드 비교를 위해 교체하기
            p = c
            c = p * 2
        # 자식 노드가 부모노드보다 더 크다면 반복 종료
        else:
            break

    return result
        

# 연산의 개수 N
N = int(input())

# 힙
heap = deque([0])
# 힙 인덱스
heap_idx = 0

# 연산
for _ in range(N):
    # 입력받기
    x = int(input())

    # 0을 입력받는다면
    if x == 0:
        # 힙의 길이가 2 초과라면 루트노드 출력
        if len(heap) > 2:
            # 힙 삭제함수로 루트노드 출력
            print(heap_sort(heap))
        # 힙의 길이가 2라면 힙에 1개만 있는 것이므로 그대로 출력
        elif len(heap) == 2:
            print(heap.pop())
            heap_idx -= 1
        # 힙이 비어있다면 0 출력
        else:
            print(0)

    # 그 외를 입력받는다면 힙 추가 및 인덱스 +1 후 힙 정렬
    else:
        heap.append(x)
        heap_idx += 1
        min_heap(heap, heap_idx)

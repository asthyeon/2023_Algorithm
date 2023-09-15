import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 연산을 지원하는 프로그램 작성
1. 연산
 - 배열에 자연수 x 넣기
 - 배열에서 가장 큰 값을 출력 및 제거
2. 0이 주어진 횟수만큼 답 출력
3. 배열이 비어있으면 0 출력
"""


# 최대 힙 함수
def max_heap(heap_idx, heap):
    # 힙의 인덱스가 루트노드일경우 종료
    if heap_idx == 1:
        return
    # 부모노드보다 자식노드가 더 크다면 교체
    if heap[heap_idx // 2] < heap[heap_idx]:
        heap[heap_idx // 2], heap[heap_idx] = heap[heap_idx], heap[heap_idx // 2]
        # 부모노드에서 다시 비교
        max_heap(heap_idx // 2, heap)
    # 부모노드보다 자식노드가 더 작다면 종료
    else:
        return


# 힙 삭제 후 출력 함수
def delete_heap(heap):
    global heap_idx
    # 최대값 저장
    result = heap[1]
    # 힙 정렬을 하기 위해 루트노드 위치로 변경 및 인덱스 줄이기
    heap[1] = heap.pop()
    heap_idx -= 1
    # 루트노드 및 자식노드 인덱스
    p = 1
    c = p * 2
    # 자식이 하나라도 있다면
    while heap_idx >= c:
        # 오른쪽 자식이 있고 오른쪽 자식이 더 크다면 교체
        if heap_idx >= c + 1 and heap[c] < heap[c + 1]:
            c += 1
        # 부모노드보다 자식노드가 더 크다면 교체
        if heap[p] < heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            # 부모노드와 자식노드 교체
            p = c
            c = p * 2
        # 자식 노드가 부모노드보다 더 크다면 반복 종료
        else:
            break
    
    # 루트노드 반환
    return result    


# 연산의 개수 N
N = int(input())

# 힙 생성
heap = [0]
heap_idx = 0

# 연산하기
for _ in range(N):
    X = int(input())
    # 0을 입력받는다면
    if X == 0:
        # 힙의 길이가 3 이상이라면 루트노드(최대값) 출력
        if len(heap) >= 3:
            print(delete_heap(heap))
        # 힙의 길이가 2라면 루트노드 출력
        elif len(heap) == 2:
            heap_idx -= 1
            print(heap.pop())
        # 힙이 비어있다면 0 출력
        else:
            print(0)

    # 그 외를 입력받는다면 힙 삽입
    else:
        heap.append(X)
        heap_idx += 1
        max_heap(heap_idx, heap)


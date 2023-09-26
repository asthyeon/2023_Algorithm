import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 입력에서 0이 주어지는 회수만큼 답 출력
1. 연산 규칙
 [1] 배열에 정수 x (x != 0)를 넣는다.
 [2] 배열에서 절댓값이 가장 작은 값 출력 및 제거
 [3] 절댓값이 가장 작은 값이 여러 개일 때는, 가장 작은 수 출력 및 배열에서 제거
2. 비어있는 배열에서 시작
@ 풀이
(1) 최소 힙 사용
(2) 절대값, 그냥값을 다 받고 같을 때도 정렬하기
(3) 출력은 그냥값
(4) 튜플로 다 묶고 정렬하기(앞에가 같으면 뒤에 숫자로 정렬함)
"""


# 최소 힙 함수
def min_heap(arr, idx):
    # 루트 노드라면 함수 종료
    if idx == 1:
        return
    # 루트 노드가 아닐 때
    else:
        # 부모 노드가 자식 노드 보다 값이 더 작다면 교체 후 부모 노드에서 재탐색
        if arr[idx] < arr[idx // 2]:
            arr[idx], arr[idx // 2] = arr[idx // 2], arr[idx]
            min_heap(arr, idx // 2)
        else:
            return


# 삭제 함수
def delete(arr):
    result = arr[1][1]
    global idx
    if idx == 1:
        idx -= 1
        arr.pop()
        return result
    arr[1] = arr.pop()
    idx -= 1
    p = 1
    c = p * 2
    # 자식이 1명이라도 있다면
    while c <= idx:
        # 오른쪽 자식이 있고 오른쪽 자식이 더 작다면
        if c + 1 <= idx and arr[c] > arr[c + 1]:
            c += 1
        # 부모 노드와 자식 노드 비교
        if arr[p] > arr[c]:
            arr[p], arr[c] = arr[c], arr[p]
            p = c
            c = p * 2
        else:
            break

    return result


# 연산의 개수 N
N = int(input())

# 연산 입력받기
commands = [(0, 0)]
idx = 0
for i in range(N):
    c = int(input())
    # 0이 아닐 때 절대값, 그냥 값 기준으로 받기
    if c != 0:
        commands.append((abs(c), c))
        idx += 1
        # 절대값 기준으로 정렬
        min_heap(commands, idx)
    else:
        # 비어있을 때는 0 출력
        if len(commands) == 1:
            print(0)
        # 비어있지 않으면 삭제 함수 사용
        else:
            print(delete(commands))




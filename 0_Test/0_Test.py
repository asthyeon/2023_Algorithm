import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# 최소 힙 함수
def min_heap(arr, idx):
    while idx > 1:
        parent_idx = idx // 2
        if arr[parent_idx] > arr[idx]:
            arr[parent_idx], arr[idx] = arr[idx], arr[parent_idx]
            idx = parent_idx
        else:
            break


# 삭제 함수
def delete(arr):
    if len(arr) <= 1:
        return 0

    result = arr[1][1]
    arr[1] = arr[-1]
    arr.pop()
    idx = 1

    while idx * 2 < len(arr):
        left_child = idx * 2
        right_child = left_child + 1

        min_child = left_child

        if right_child < len(arr) and arr[right_child] < arr[left_child]:
            min_child = right_child

        if arr[idx] > arr[min_child]:
            arr[idx], arr[min_child] = arr[min_child], arr[idx]
            idx = min_child
        else:
            break

    return result


# 연산의 개수 N
N = int(input())

# 연산 입력받기
commands = [(0, 0)]  # (절댓값, 원래 값)
idx = 0
for _ in range(N):
    command = int(input())
    if command != 0:
        commands.append((abs(command), command))
        idx += 1
        min_heap(commands, idx)
    else:
        if len(commands) == 1:
            print(0)
        else:
            print(delete(commands))
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 명령 처리 프로그램
1. push X: 정수 X를 큐에 넣음
2. pop: 큐에서 가장 앞 정수를 빼고 출력, 큐에 정수가 없는 경우 -1 출력
3. size: 큐에 들어있는 정수 개수 출력
4. empty: 큐가 비어있으면 1, 아니면 0 출력
5. front: 큐의 가장 앞 정수 출력, 정수가 없는 경우 -1
6. back: 큐의 가장 뒤 정수 출력, 정수가 없는 경우 -1

# pop, del, remove 이용하면 시간초과
'''

# 명령의 수
N = int(input())

# 큐
queue_list = []
# 시간초과를 막기 위해서 현재 위치를 사용하기
top = 0

for i in range(1, N + 1):
    command = input().split()

    # 1. push
    if command[0] == 'push':
        queue_list.append(int(command[1]))

    # 2. pop
    if command[0] == 'pop':
        if len(queue_list) - top > 0:
            print(queue_list[top])
            top += 1
        else:
            print(-1)

    # 3. size
    if command[0] == 'size':
        print(len(queue_list) - top)

    # 4. empty
    if command[0] == 'empty':
        if len(queue_list) - top > 0:
            print(0)
        else:
            print(1)

    # 5. front
    if command[0] == 'front':
        if len(queue_list) - top > 0:
            print(queue_list[top])
        else:
            print(-1)

    # 6. back
    if command[0] == 'back':
        if len(queue_list) - top > 0:
            print(queue_list[-1])
        else:
            print(-1)
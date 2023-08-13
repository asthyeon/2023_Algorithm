import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하기
1. x: 정수 x를 스택에 넣는다. (1 <= X <= 100,000)
2. 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1 을 대신 출력한다.
3. 스택에 들어있는 정수의 개수를 출력한다.
4. 스택이 비어있으면 1, 아니면 0 을 출력한다.
5. 스택에 정수가 있다면 맨 위으 정수를 출력한다. 없다면 -1 을 대신 출력한다.
'''

# 명령의 수: N
N = int(input())

# stack 형성
stack = []

for tc in range(N):
    # 명령 입력받기
    command = list(map(int, input().split()))

    # 1. 정수 x를 스택에 넣기
    if command[0] == 1:
        stack.append(command[1])

    # 2. 스택에 정수 있으면 pop() 출력, 없으면 -1 출력
    elif command[0] == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)

    # 3. 스택에 들어있는 정수의 개수 출력
    elif command[0] == 3:
        print(len(stack))

    # 4. 스택이 비어있으면 1, 아니면 0 출력
    elif command[0] == 4:
        if not stack:
            print(1)
        else:
            print(0)

    # 5. 스택에 정수가 있다면 맨 위의 정수 출력, 없으면 -1 출력
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)



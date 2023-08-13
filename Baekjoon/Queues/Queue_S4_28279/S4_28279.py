import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
'''
1. x: 정수 x를 덱의 앞 추가
2. x: 정수 x를 덱의 뒤 추가
3. 덱에 정수가 있다면 맨 앞 빼고 출력, 없으면 -1
4. 덱에 정수가 있다면 맨 뒤 빼고 출력, 없으면 -1
5. 덱에 들어있는 정수 개수
6. 덱이 비어있으면 -1, 아니면 0 출력
7. 덱에 정수가 있다면 맨 앞 출력, 없으면 -1
8. 덱에 정수가 있다면 맨 뒤 출력, 없으면 -1
# 시간초과로 결국 내장함수 사용
'''

# 명령의 수
N = int(input())

# 덱 구현
deck = deque()

# 현재 위치
top = 0
# 역순 위치
reverse = -1

for i in range(N):
    command = list(map(int, input().split()))

    # 1번
    if command[0] == 1:
        deck.appendleft(command[1])
        reverse += 1

    # 2번
    if command[0] == 2:
        deck.append(command[1])
        reverse += 1

    # 3번
    if command[0] == 3:
        if len(deck) > 0:
            print(deck.popleft())
        else:
            print(-1)

    # 4번
    if command[0] == 4:
        if len(deck) - top > 0:
            print(deck.pop())
        else:
            print(-1)

    # 5번
    if command[0] == 5:
        print(len(deck))

    # 6번
    if command[0] == 6:
        if len(deck) > 0:
            print(0)
        else:
            print(1)

    # 7번
    if command[0] == 7:
        if len(deck) > 0:
            print(deck[0])
        else:
            print(-1)

    # 8번
    if command[0] == 8:
        if len(deck) > 0:
            print(deck[-1])
        else:
            print(-1)

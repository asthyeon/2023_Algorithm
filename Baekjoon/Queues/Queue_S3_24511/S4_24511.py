import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
'''
# 큐스택
1. x0 을 입력
2. x0 을 1번 자료구조에 삽입, 1번 자료구조에서 원소 pop, pop된 원소: x1
3. x1 을 2번 자료구조에 삽입, 2번 자료구조에서 원소 pop, pop된 원소: x2
4. x(N-1) 을 N번 자료구조에 삽입, 2번 자료구조에서 원소 pop, pop된 원소: xN
5. xN 리턴
6. 수열 C를 차례대로 큐스택에 삽입
7. 큐일 때 왼쪽에 삽입, 스택일 때는 그대로
8. 시간초과로 내장함수 사용
'''

# 자료구조 개수 N
N = int(input())

# N 의 수열 A
A = list(map(int, input().split()))

# N 의 수열 B
B = list(map(int, input().split()))

# 수열의 길이
M = int(input())

# 큐스택에 삽입할 원소를 담고 있는 수열 C
C = list(map(int, input().split()))

# queue 일 때 만 고려하기
queue = deque()

# 큐인 부분만 미리 큐에 넣어놓기
for i in range(N):
    # 큐일 때
    if A[i] == 0:
        # 큐인 부분은 원소가 교체되기 때문에 나중의 것을 출력하기 위해 append
        queue.append(B[i])

# 각 원소들이 맨앞으로 가는 것을 이용하여 하나씩 밀어내서 출력하기
for t in C:
    # 새로 원소가 들어올경우 큐일 경우 맨 앞으로 감
    queue.appendleft(t)
    # 쌓인 큐를 출력
    print(queue.pop(), end = ' ')



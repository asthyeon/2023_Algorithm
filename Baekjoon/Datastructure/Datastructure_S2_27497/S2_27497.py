import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque
'''
# 버튼을 누른 횟수와 누른 버튼이 순서대로 주어질 때 완성된 문자열 구하기
1. 문자열 맨 뒤에 블록 추가
2. 문자열 맨 앞에 블록 추가
3. 문자열을 구성하는 블록 중 가장 나중에 추가된 블록 제거
'''

# 누른 횟수
N = int(input())

# 문자열
string = deque()

# 스택
stack = []

# 중복조건
duple = []

for i in range(N):
    # 버튼 입력
    button = input().split()
    
    # 1 일 때 맨 뒤에 붙이기
    if button[0] == '1':
        string.append(button[1])
        stack.append(button[1])
        # 중복확인용
        duple.append('L')
    
    # 2 일 때 맨 앞에 붙이기
    if button[0] == '2':
        string.appendleft(button[1])
        stack.append(button[1])
        # 중복확인용
        duple.append('F')
    
    # 3 일 때 가장 나중에 추가된 블록 제거
    if button[0] == '3':
        # stack 이 비어 있지 않다면
        if stack:
            # stack 이 처음이 아니라면
            if len(stack) > 1:
                # 첫 항과 막 항이 중복이 아니라면
                if string[0] != string[-1]:
                    # 마지막 스택이 문자열 첫글자와 같다면 왼쪽 제거
                    if stack[-1] == string[0]:
                        string.popleft()
                        stack.pop()
                        duple.pop()
                    # 다르다면 오른쪽 제거
                    else:
                        string.pop()
                        stack.pop()
                        duple.pop()
                # 중복이라면
                else:
                    # 맨 앞이 최근이라면 왼쪽 제거
                    if duple[-1] == 'F':
                        string.popleft()
                        stack.pop()
                        duple.pop()
                    # 맨 뒤가 최근이라면 오른쪽 제거
                    else:
                        string.pop()
                        stack.pop()
                        duple.pop()
            # stack 이 처음이라면
            else:
                string.pop()
                stack.pop()
                duple.pop()
        # stack 이 비어있지 않다면 계속
        else:
            continue
                
# 문자열이 비어있지 않다면
if string:
    print(*string, sep = '')
# 비어있다면
else:
    print(0)
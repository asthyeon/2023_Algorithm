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

for i in range(N):
    # 버튼 입력
    button = input().split()
    
    # 1 일 때 맨 뒤에 붙이기
    if button[0] == '1':
        string.append(button[1])
        stack.append(button[1])
    
    # 2 일 때 맨 앞에 붙이기
    if button[0] == '2':
        string.appendleft(button[1])
        stack.append(button[1])
    
    # 3 일 때 가장 나중에 추가된 블록 제거
    if button[0] == '3':
        # stack 이 비어 있지 않다면
        if stack:
            # 첫 항과 막 항이 중복이 아니라면
            if string[0] != string[-1]:
                # 마지막 스택이 문자열 첫글자와 같다면 왼쪽 제거
                if stack[-1] == string[0]:
                    string.popleft()
                    stack.pop()
                # 다르다면 오른쪽 제거
                else:
                    string.pop()
                    stack.pop()
            # 중복이라면
            else:
                
# 문자열이 비어있지 않다면
if string:
    print(*string, sep = '')
# 비어있다면
else:
    print(0)
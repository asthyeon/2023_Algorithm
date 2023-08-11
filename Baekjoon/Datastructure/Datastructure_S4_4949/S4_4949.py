import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 괄호들의 균형을 맞추기
1. 모든 괄호는 짝을 이뤄야 함
2. 짝을 이루는 두 괄호 사이의 문자열도 균형 잡혀야 함
'''

while True:
    sentence = input().rstrip()

    # while 문 종료 조건
    if sentence == '.':
        break

    # stack 형성
    stack = []
    top = -1

    # sentence 만큼 반복
    for t in sentence:
        # 종료조건
        if t == '.':
            break
        # 왼쪽 소괄호
        if t == '(':
            stack.append(t)
            top += 1
        # 오른쪽 소괄호
        elif t == ')':
            stack.append(t)
            top += 1
            # top 이 1 보다 크다면
            if top > 0:
                # 직전 스택이 '(' 이라면 짝 제거
                if stack[top - 1] == '(':
                    stack.pop()
                    stack.pop()
                    top -= 2
                # 그게 아니라면 반복 종료
                else:
                    break
        # 왼쪽 대괄호
        if t == '[':
            stack.append(t)
            top += 1
        # 오른쪽 대괄호
        elif t == ']':
            stack.append(t)
            top += 1
            # top 이 1 보다 크다면
            if top > 0:
                # 직전 스택이 '[' 이라면 짝 제거
                if stack[top - 1] == '[':
                    stack.pop()
                    stack.pop()
                    top -= 2
                # 그게 아니라면 반복 종료
                else:
                    break
            # top 이 1 보다 작다면
            else:
                break

    if stack:
        print('no')
    else:
        print('yes')







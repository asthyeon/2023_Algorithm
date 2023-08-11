import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 괄호 문자열이 VPS 인지 아닌지를 판단하기
1. VPS = 괄호의 모양이 바르게 구성된 문자열
'''

T = int(input())
for tc in range(1, T + 1):
    vps = input().strip()

    # stack 형성
    stack = []
    top = -1

    # vps 길이만큼 반복
    for i in range(len(vps)):
        # i == 0 일 때는 따로 설정
        if i == 0:
            # 왼쪽 소괄호라면
            if vps[i] == '(':
                stack.append(vps[i])
                top += 1
            # 오른쪽 소괄호라면 push 후 반복 종료
            else:
                stack.append(vps[i])
                break
        # 인덱스 1 번째부터
        else:
            # 왼쪽 소괄호라면 push
            if vps[i] == '(':
                stack.append(vps[i])
                top += 1
            # 오른쪽 소괄호라면 일단 push 후
            else:
                stack.append(vps[i])
                top += 1
                # top 이 0 보다 크다면
                if top > 0:
                    # 직전 스택의 top 값과 대칭이라면 pop
                    if stack[top - 1] == '(':
                        stack.pop()
                        stack.pop()
                        top -= 2
                # top 이 0 이라면 반복 종료
                else:
                    break
    # 정답 조건
    if stack:
        print('NO')
    else:
        print('YES')
        
        
        
        
        
        
        
        
        
        
        
            
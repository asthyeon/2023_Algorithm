import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 정수가 0일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다
1. 최종적으로 적어낸 수의 합을 출력하기
'''

K = int(input())

# stack 형성
stack = []

for _ in range(K):
    N = int(input())

    # 정수가 0 보다 크면 stack push
    if N > 0:
        stack.append(N)
    # 정수가 0 이라면 pop()
    else:
        stack.pop()

print(sum(stack))
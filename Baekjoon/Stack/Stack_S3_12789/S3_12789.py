import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 줄서기 프로그램
1. 1열로 줄을 서있고, 맨 앞의 사람만 이동이 가능
2. 번호표 순서대로만 통과할 수 있는 라인 존재
3. 이 라인과 대기열의 맨 앞 사람 사이에는 한 사람씩 1열이 들어갈 수 있는 공간 존재
4. 현재 대기열의 사람들은 들어올 수 있지만 반대는 불가능
'''

# 승환이 앞의 학생의 수
N = int(input())

# 모든 학생들의 번호표
numb = list(map(int, input().split()))

# 간식 받는 곳의 번호 표
arr = [0] * len(numb)
for i in range(len(numb)):
    arr[i] = i + 1

# 간식 받는 곳
goal = []

# stack 형성(대기공간)
stack = []

# 정답조건
ans = 1

# 순서용
i = 0

while i < len(arr):
    # 현재 줄 서 있는 곳에 사람이 있을 때
    if numb:
        if arr[i] == numb[0]:
            goal.append(numb.pop(0))
        # 번호표가 맞지 않는다면
        else:
            # stack 이 빈 칸이 아닐 때 최근 값과 stack 과 비교
            if stack:
                # 스택의 top 값과 같다면 stack top 제거
                if arr[i] == stack[-1]:
                    goal.append(stack.pop())
                # 다르다면 push
                else:
                    stack.append(numb.pop(0))
            # 빈 칸이 아니라면 push
            else:
                stack.append(numb.pop(0))
    # 현재 줄 서 있는 곳에 사람이 없을 때 -> stack 비교
    else:
        if stack:
            # 스택의 top 값과 같다면 stack top 제거
            if arr[i] == stack[-1]:
                goal.append(stack.pop())
            # 다르다면
            else:
                # 현재 줄 서 있는 곳이 차있다면 push
                if numb:
                    stack.append(numb.pop(0))
                # 비어있다면 반복 종료
                else:
                    ans = 0
                    break
        # 빈 칸이 아니라면 push
        else:
            stack.append(numb.pop(0))
    # goal 에 누군가 들어 갔다면 다음 순서
    if len(goal) == i + 1:
        i += 1
    if ans == 0:
        break

if len(goal) == len(arr):
    print('Nice')
else:
    print('Sad')


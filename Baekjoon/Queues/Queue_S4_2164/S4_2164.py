import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
1. 제일 위 카드 버리기
2. 제일 위 카드를 제일 아래 카드 아래로 옮기기
3. 1장 남을 때까지 반복
# 제일 마지막에 남는 카드 구하기
'''

# N 장의 카드리스트 만들기
N = int(input())
arr = [0] * N
for i in range(N):
    arr[i] = i + 1

# 시간초과를 막기 위한 현재 위치
top = 0

# arr 의 길이가 1이 될 때 까지 반복
while len(arr) - top > 1:
    # 제일 위 카드 삭제
    top += 1
    # 제일 위 카드를 맨 뒤로 옮기기
    queue = arr[top]
    top += 1
    arr.append(queue)

print(arr[-1])







import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 입력으로 주어지는 사용할 벽장의 순서에 따라서 벽장문을 이동하는 순서 찾기(이동횟수 최소)
1. n개의 같은 크기의 벽장들이 일렬로 붙어져 있고 벽장의 문은 n-2만이 존재
2. 한 벽장 앞에 있는 문은 이웃 벽장 앞에 문이 없다면(열려있다면) 벽장 앞으로 움직일 수 있음
3. 벽장 문은 좌우 어느 쪽이든 그 이웃 벽장이 열려 있다면 그 쪽으로 한 칸씩 이동 가능
4. 열려 있는 벽장의 개수는 항상 2개
@ 풀이
(1) dp로 풀기
(2) 벽장문이 현재 열려 있는 문 사이로 들어오면 분기를 나눌 것
"""


# dp 함수
def dynamic_programming():
    # dp 행렬
    dp1 = [0] * n
    dp2 = [0] * n

    for i in range(length):
        # 이번에 사용할 벽장
        target = numbers[length]
        # 벽장이 현재 열린 벽장 사이에 있을 경우 분기 나누기
        if open1 - 1 < target - 1 < open2 - 1:
            # 왼쪽 dp
            # 이전에 open1에 도착한 값
            move = dp1[open1 - 1]
            for j in range(open1 + 1, target + 1):
                dp1[j] = move + 1
                move = dp1[]



# 벽장의 개수
n = int(input())
# 열려있는 벽장문
open1, open2 = map(int, input().split())
# 사용할 벽장들의 순서의 길이
length = int(input())
# 각 벽장들의 문 상태(0: 열림, 1: 닫힘)
cupboards = []
for i in range(1, n + 1):
    if i == open1 or i == open2:
        cupboards.append(0)
    else:
        cupboards.append(1)

# 사용할 벽장의 번호
numbers = []
for _ in range(length):
    number = int(input())
    numbers.append(number)

"""
# 예제
7
2 5
4
3
1
6
5
0: 1 0 1 1 0 1 1

0: 1 1 0 1 0 1 1
3: 0 1 0 0 0 0 0
0: 1 0 0 1 1 1 1
3: 0 0 0 2 1 0 0

0: 0 1 1 1 0 1 1
1: 0 3 2 0 0 0 0
0: 0 1 0 1 1 1 1



# 반례
8
3 8
2
5
1
0: 1 1 0 1 1 1 1 0

0: 1 1 1 1 0 1 1 0
5: 0 0 1 2 0 0 0 0
0: 1 1 0 1 0 1 1 1
5: 0 0 0 0 0 3 2 1 

0: 0 1 1 1 1 1 1 0
1: 0 6 5 4 3 0 0 0
0: 0 1 1 1 0 1 1 1
1: 0 5 4 0 0 3 2 1
"""





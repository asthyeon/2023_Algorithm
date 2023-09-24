import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# N x N 인 체스판 위에 퀸 N 개를 서로 공격할 수 없게 하는 경우의 수
1. N-Queen 문제
@ 풀이
(1) 백트래킹으로 풀기
(2) 첫 줄에 놓으면 다음 줄에 놓는 경우의 수를 생각하기
(3) 반복을 줄이기 -> 2차원 배열 사용 X
(4) 대각선에 놓이는 조건: 놓인 좌표의 차이 == 인덱스의 차이
"""


# 백트래킹 함수
def backtracking(N, path, Q):
    global cnt
    # 재귀를 종료하는 기저 조건
    if Q == N:
        cnt += 1
        return

    for i in range(N):
        # 넘기기 위한 조건
        skip = False
        path[Q] = i
        # 모든 행을 돌며
        for j in range(Q):
            # 같은 열에 놓여있거나 대각선에 놓여있을 경우 넘기기
            if path[j] == path[Q] or abs(path[j] - path[Q]) == abs(j - Q):
                skip = True
                break
        if skip:
            continue
        Q += 1
        backtracking(N, path, Q)
        Q -= 1


# 체스판의 크기 N
N = int(input())

# 퀸이 놓여진 수
Q = 0
# 퀸을 N 개 놓는 경우의 수
cnt = 0
# 퀸을 놓은 상태
path = [0] * N

backtracking(N, path, Q)
print(cnt)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 모든 빈 칸이 채워진 최종 모습 출력하기
1. 각각의 가로줄과 세로줄에는 1부터 9까지의 숫자가 한 번씩만 나타나야함
2. 굵은 선으로 구분되어 있는 3x3 정사각형 안에서도 1부터 9까지의 숫자가 한 번씩만 나타나야함
3. 스도쿠 판을 채울 수 없는 경우의 입력 X
4. 스도쿠 판을 채우는 방법이 여럿인 경우 그 중 하나만을 출력
@ 풀이
(1) 백트래킹으로 풀기
(2) 가로, 세로, 정사각형의 경우의 수 모두 고려하기
"""


# 가로 확인
def row(x, num):
    for n in range(9):
        if num == sudoku[x][n]:
            return False
    return True


# 세로 확인
def col(y, num):
    for n in range(9):
        if num == sudoku[n][y]:
            return False
    return True


# 정사각형 확인
def square(x, y, num):
    x = x // 3 * 3
    y = y // 3 * 3
    for r in range(3):
        for c in range(3):
            if num == sudoku[x + r][y + c]:
                return False
    return True


# 백트래킹 함수
def backtracking(sudoku, cnt):
    # 재귀를 종료할 기저 조건
    # 모든 빈칸을 채웠다면 종료
    if cnt == len(zeros):
        for i in range(9):
            print(*sudoku[i])
        exit()

    # 1 ~ 9 까지 숫자를 넣는 반복문
    for num in range(1, 10):
        # 0인 좌표를 가져오기
        x, y = zeros[cnt]
        if row(x, num) and col(y, num) and square(x, y, num):
            sudoku[x][y] = num
            cnt += 1
            backtracking(sudoku, cnt)
            cnt -= 1
            sudoku[x][y] = 0


# 스도쿠 판 입력
sudoku = [list(map(int, input().split())) for _ in range(9)]

# 스도쿠 판에서 0 인 위치 확인
zeros = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append((i, j))

# 모든 위치를 채웠는지 확인하기 위한 변수
cnt = 0

backtracking(sudoku, cnt)
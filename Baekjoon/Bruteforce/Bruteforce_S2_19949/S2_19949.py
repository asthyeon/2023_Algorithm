import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10 * 6)

"""
# 영재의 점수가 5점 이상일 경우의 수 구하기
1. 1문제당 1점
2. 5지 선다의 객관식 10문제
3. 3개의 연속된 문제의 답은 같지 않게 함
@ 풀이
(1) 백트래킹으로 풀기
(2) 경우의 수를 구해야하므로 가지치기 X
"""


# 백트래킹 함수
def backtracking(path, num, grades):
    global cnt
    # 재귀를 종료할 기저 조건
    if num == 10:
        if grades[-1] >= 5:
            cnt += 1
        return

    # 경우의 수 구하기
    for i in range(1, 6):
        # 3개 연속 찍을 수 없기 때문에 이전과 전이 같다면 다르게 해주기
        if num >= 2:
            if path[num - 2] == path[num - 1]:
                if path[num - 1] == i:
                    continue
        path[num] = i
        # 정답인지 미리 확인
        if num >= 1:
            grades[num] = grades[num - 1]
        if path[num] == answers[num]:
            grades[num] += 1
        num += 1
        backtracking(path, num, grades)
        num -= 1
        path[num] = 0
        grades[num] = 0


# 정답
answers = list(map(int, input().split()))

# 경우의 수 구하기
path = [0] * 10
cnt = 0
num = 0
# 점수를 기록할 리스트
grades = [0] * 10

backtracking(path, num, grades)
print(cnt)
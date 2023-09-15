import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 마지막 기록 이후 무지개 댄스 추는 사람은 몇명인가?
1. 사람들이 만난 기록이 시간 순서대로 N개 주어짐
2. 무지개 댄스 안추는 사람이 추는 사람 만나면 이후로 댄스
3. 기록이 시작되기 전에는 총총이 뿐
"""

# 사람들이 만난 기록의 수 N
N = int(input())
# 사람들 딕셔너리
N_list = {}

# 사람들이 만난 기록
for _ in range(N):
    A, B = map(str, input().split())

    # 처음 나오는 사람들일 경우 0 넣기
    if A not in N_list:
        N_list[A] = 0
        # 총총이인 경우 1
        if A == 'ChongChong':
            N_list[A] = 1
    if B not in N_list:
        N_list[B] = 0
        # 총총이인 경우 1
        if B == 'ChongChong':
            N_list[B] = 1

    # 1인 사람과 만난다면 0인 사람은 1로 바꿔주기
    if N_list[A] == 1 or N_list[B] == 1:
        N_list[A] = 1
        N_list[B] = 1

# 1인 사람(댄스추는사람)이라면 cnt += 1
cnt = 0
for dancer in N_list:
    if N_list[dancer] == 1:
        cnt += 1

print(cnt)

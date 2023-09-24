import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 해야 한다
1. 짝수 N 명이 축구하러 모임
2. N/2 명으로 이루어진 스타트 팀 vs 링크 팀
@ 풀이
(1) 백트래킹으로 풀기
"""


# 백트래킹 함수
def backtracking(start, stats, cnt, idx):
    global min_differ
    # 재귀를 종료하는 기저조건(스타트 리스트가 다 찼을 때)
    if cnt == N // 2:
        sum_start = 0
        sum_link = 0
        # 각 리스트를 비교하여 능력치의 합 구하기
        for x in range(N):
            for y in range(N):
                # 0이 아니라면 start, 0이라면 link
                if start[x] and start[y]:
                    sum_start += stats[x][y]
                elif not start[x] and not start[y]:
                    sum_link += stats[x][y]
        # 능력치의 최소차이 구하기
        differ = abs(sum_start - sum_link)
        if min_differ > differ:
            min_differ = differ
        return
    
    # 스타트 팀과 링크 팀이 겹치지 않게 팀원을 뽑기
    for i in range(idx, N):
        if i in used:
            continue
        start[i] = 1
        used.append(i)
        cnt += 1
        backtracking(start, stats, cnt, i + 1)
        cnt -= 1
        used.pop()
        start[i] = 0


# 축구 인원
N = int(input())

# 능력치판
stats = [list(map(int, input().split())) for _ in range(N)]

# 스타트팀
start = [0] * (N)
used = []
cnt = 0
idx = 0
# 두 팀의 능력치 차이
min_differ = 10000
backtracking(start, stats, cnt, idx)
print(min_differ)
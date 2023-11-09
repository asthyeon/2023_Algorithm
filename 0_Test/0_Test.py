import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 문자열마다 경우의 수 출력
1. M x N 행렬은 환형
2. 상하좌우대각선 이동 가능, 지나온 칸 다시 방문 가능
3. 방문 순서가 다르면 다른 경우
4. 중복된 문자열이 들어올 수 있음
@ 풀이
(1) 재귀를 이용하여 모든 경우의 수 탐색
(2) 중복은 딕셔너리에 넣어서 처리
"""
# 8방향 탐색을 위한 튜플
ds = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]
# 중복 문자열 방지
duple = {}


# 탐색(시작좌표, 단어를 찾은 길이, 배열)
def searching(sx, sy, find, arr):
    global cnt
    # 다 찾았다면 경우의 수 +1
    if find == len(word):
        cnt += 1
        return
    # 8방향 탐색
    for dx, dy in ds:
        nx, ny = sx + dx, sy + dy
        # 벽 형성
        if 0 <= nx < N and 0 <= ny < M:
            # 해당 단어가 이번에 찾을 단어와 일치한다면 재귀
            if arr[nx][ny] == word[find]:
                searching(nx, ny, find + 1, arr)
        # 벽을 넘어갈 시
        else:
            if nx < 0:
                nx = N + nx
            elif nx >= N:
                nx = nx - N
            if ny < 0:
                ny = M + ny
            elif ny >= M:
                ny = ny - M
            # 해당 단어가 이번에 찾을 단어와 일치한다면 재귀
            if arr[nx][ny] == word[find]:
                searching(nx, ny, find + 1, arr)


# 세로 N, 가로 M, 문자열 수 K
N, M, K = map(int, input().split())
# 격자판
arr = [input().rstrip() for _ in range(N)]
# 문자열 정보
for _ in range(K):
    word = input().rstrip()
    # 경우의 수
    cnt = 0
    # 중복이 아니라면 탐색
    if word not in duple:
        # 탐색
        for sx in range(N):
            for sy in range(M):
                if arr[sx][sy] == word[0]:
                    searching(sx, sy, 1, arr)
        duple[word] = cnt
        print(cnt)
    # 중복이라면
    else:
        print(duple[word])
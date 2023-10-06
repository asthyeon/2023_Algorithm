import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


"""
# 백준시를 두 선거구로 나누었을 때 인구 차이의 최솟값 출력
1. 각 선거구는 서로 연결되어 있어야 함
2. 양방향 인접
3. 두 선거구로 나눌 수 없는 경우 -1 출력
@ 풀이
(1) dfs 로 구역 하나를 구하고 다른 구역은 bfs 로 구한 후
(2) 두 개의 길이를 더한 것이 N이 된다면 인구수 차이 계산하기
"""
from collections import deque


# dfs 함수
def dfs(n):
    # 방문 리스트
    visited = [0] * (N + 1)
    # 스택 생성 및 시작점 푸쉬
    stack = []
    # 시작점 방문기록
    visited[n] = 1
    while True:
        length = len(stack) + 1
        bfs(n, length, area)
        for w in range(1, N + 1):
            # 인접해있고 방문하지 않았다면
            if adj[n][w] == 1 and visited[w] == 0:
                # 지나온 곳 스택에 넣기
                stack.append(n)
                # 위치 변경
                n = w
                # 방문 표시
                visited[n] = 1
                # 인접인 곳 찾았기 때문에 반복 종료
                break
        # 인접한 곳이 없다면
        else:
            # 스택에 지나온 곳이 남아있다면
            if stack:
                # 지나온 곳으로 다시 돌아가서 인접한 곳 다시 찾기
                n = stack.pop()
            # 스택이 비어있으면 탐색 종료
            else:
                break
    return


# bfs 함수
def bfs(s, length, area):
    global result
    # 방문 배열
    visited2 = [0] * (N + 1)
    # 큐 생성 및 시작점 인큐
    q = deque([s])
    # 방문 기록
    visited2[s] = 1
    # 큐가 빌 때까지
    while q:
        # 디큐
        t = q.popleft()
        # 인접 지역 찾기
        for w in range(1, N + 1):
            if adj[t][w] == 1 and visited2[w] == 0:
                q.append(w)
                visited2[w] = visited2[t] + 1
    for i in range(1, N + 1):
        if (visited2[i] - 1) + length == N:
            break
        else:
            return
    area1 = 0
    area2 = 0
    for j in range(1, N + 1):
        if visited2[j] != 0:
            area1 += area[j - 1]
        else:
            area2 += area[j - 1]
    if area1 > area2:
        differ = area1 - area2
    else:
        differ = area2 - area1
    if result > differ:
        result = differ


# 구역의 개수 N
N = int(input())
# 각 구역의 인구수
area = list(map(int, input().split()))
# 인접배열
adj = [[0] * (N + 1) for _ in range(N + 1)]

# 인접 구역 연결
for i in range(1, N + 1):
    # 인접 정보
    adj_info = list(map(int, input().split()))
    for j in range(1, adj_info[0] + 1):
        adj[i][adj_info[j]] = 1
        adj[adj_info[j]][i] = 1

# 인구수 차이
result = 100000000000000

# 브루트포스 탐색
for n in range(1, N + 1):
    dfs(n)

if result == 100000000000000:
    print(-1)
else:
    print(result)
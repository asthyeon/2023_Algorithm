import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 선거구를 두 개로 나누었을 때, 인구의 차이를 최소로 하기
1. 각 선거구는 구역을 적어도 하나 포함
2. 각 선거구는 연결되어 있어야 함
3. 두 선거구로 나눌 수 없는 경우 -1 출력
@ 풀이
(1) dfs 로 하나씩 이동하고 bfs 로 나머지 선거구 성립 되는지 확인
"""
from collections import deque


# dfs 함수
def dfs(n, populations, adj):
    dfs_pop = 0
    # 방문 리스트
    visited = [0] * (N + 1)
    # 스택 생성
    stack = []
    # 선거구의 길이
    dfs_length = 0
    # 시작점 방문 표시
    visited[n] = 1
    dfs_length += 1
    dfs_pop += populations[n - 1]
    bfs(visited, populations, dfs_pop, dfs_length, adj)
    while True:
        # 인접 구역 탐색
        for w in adj[n]:
            # 방문하지 않았다면
            if visited[w] == 0:
                stack.append(n)
                dfs_pop += populations[n - 1]
                dfs_length += 1
                n = w
                visited[n] = 1
                break
        # 인접한 구역을 다 돌았다면
        else:
            # 스택이 비어있지 않다면
            if stack:
                dfs_pop -= populations[n - 1]
                dfs_length -= 1
                n = stack.pop()
                continue
            # 스택이 비어있다면 반복 종료
            else:
                break
        bfs(visited, populations, dfs_pop, dfs_length, adj)


# bfs 함수
def bfs(visited, populations, dfs_pop, dfs_length, adj):
    global min_pop
    bfs_pop = 0
    start = 0
    # 새로운 방문리스트
    visited2 = visited[:]
    # 방문하지 않은 곳 시작점 찾기
    for i in range(1, N + 1):
        if visited2[i] == 0:
            start = i
            break
    if start == 0:
        return
    # 선거구의 길이
    bfs_length = 0
    # 큐 생성 및 시작점 인큐
    q = deque([start])
    # 시작점 방문기록
    visited2[start] = 1
    # 큐가 빌 때까지
    while q:
        n = q.popleft()
        bfs_pop += populations[n - 1]
        bfs_length += 1
        for w in adj[n]:
            # 방문하지 않은 곳이라면
            if visited2[w] == 0:
                q.append(w)
                visited2[w] = 1
    # 두 선거구로 나뉘는지 확인
    if dfs_length + bfs_length != N:
        return
    # 두 선거구로 나뉘었다면
    differ = abs(dfs_pop - bfs_pop)
    if min_pop > differ:
        min_pop = differ


# 구역의 개수 N
N = int(input())

# 각 구역의 인구 수
populations = list(map(int, input().split()))

# 인접 리스트
adj = [[] for _ in range(N + 1)]

# 각 구역과 인접한 구역의 정보
for i in range(1, N + 1):
    # 첫 번째 정수는 인접한 구역의 수, 이후 인접한 구역의 번호
    info = list(map(int, input().split()))
    
    # 인접한 구역 연결
    for j in range(1, info[0] + 1):
        adj[i].append(info[j])

# 인구 최소 차이
min_pop = 1000000000

for j in range(1, N + 1):
    dfs(1, populations, adj)

if min_pop == 1000000000:
    print(-1)
else:
    print(min_pop)
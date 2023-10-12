import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 선거구를 두 개로 나누었을 때, 인구의 차이를 최소로 하기
1. 각 선거구는 구역을 적어도 하나 포함
2. 각 선거구는 연결되어 있어야 함
3. 두 선거구로 나눌 수 없는 경우 -1 출력
@ 풀이
(1) 조합을 사용하여 선거구를 나누기
(2) 그래프 탐색 사용(dfs or bfs)
"""
from collections import deque

sys.setrecursionlimit(10 * 9)


# dfs 함수
def dfs(n, populations, adj, stack, passed, dfs_pop, dfs_length):
    # 방문한 곳이라면 빠져나오기
    if passed[n] == 1:
        return
    # 스택 형성 및 시작점 푸쉬
    stack.append(n)
    # 시작점 방문 처리
    passed[n] = 1
    # 1지역 선거구 인구수
    dfs_pop += populations[n - 1]
    # 1지역 선거구 길이
    dfs_length += 1
    # bfs 함수 사용
    # bfs(passed, populations, dfs_pop, dfs_length, adj, stack)
    # 탐색
    for w in adj[n]:
        dfs(w, populations, adj, stack, passed, dfs_pop, dfs_length)
    # 탐색을 다 돌았다면 뒤로 가기
    else:
        stack.pop()
        dfs_pop -= populations[n - 1]
        dfs_length -= 1
        passed[n] = 0


# bfs 함수
def bfs(passed, populations, dfs_pop, dfs_length, adj, stack):
    global min_pop
    # 2지역 선거구 인구수
    bfs_pop = 0
    # 새로운 방문리스트
    visited = passed[:]
    # 방문하지 않은 곳 시작점 찾기
    start = 0
    for i in range(1, N + 1):
        if visited[i] == 0:
            start = i
            break
    if start == 0:
        return
    # 선거구의 길이
    bfs_length = 0
    # 큐 생성 및 시작점 인큐
    q = deque([start])
    # 시작점 방문기록
    visited[start] = 1
    # 큐가 빌 때까지
    while q:
        n = q.popleft()
        bfs_pop += populations[n - 1]
        bfs_length += 1
        for w in adj[n]:
            # 방문하지 않은 곳이라면
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1
    # 두 선거구로 나뉘는지 확인
    if dfs_length + bfs_length != N:
        return True
    # 두 선거구로 나뉘었다면
    else:
        # 최소값으로 교체
        differ = abs(dfs_pop - bfs_pop)
        if min_pop > differ:
            min_pop = differ
        return True


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
    # 지나온 길
    passed = [0] * (N + 1)
    stack = []
    # 1지역 선거구 인구수
    dfs_pop = 0
    # 1지역 선거구 길이
    dfs_length = 0
    # dfs 함수 사용
    dfs(1, populations, adj, stack, passed, dfs_pop, dfs_length)

if min_pop == 1000000000:
    print(-1)
else:
    print(min_pop)
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


# bfs 함수
def bfs(path):
    # 방문 리스트
    visited = [0] * (N + 1)
    # 큐 생성 및 시작점 인큐
    q = deque([path[0]])
    # 시작점 방문 기록
    visited[path[0]] = 1
    # 큐가 빌 때까지
    while q:
        start = q.popleft()
        for w in adj[start]:
            if visited[w] == 0:
                visited[w] = 1
    for p in path:
        if visited[p] != 1:
            return False
    return bfs2(path)


# bfs2 함수
def bfs2(path):
    other_path = list(reverse_path.difference(path))
    visited = [0] * (N + 1)
    # 큐 생성 및 시작점 인큐
    q = deque([other_path[0]])
    # 시작점 방문 기록
    visited[other_path[0]] = 1
    # 큐가 빌 때까지
    while q:
        start = q.popleft()
        for w in adj[start]:
            if visited[w] == 0:
                visited[w] = 1
    for o in other_path:
        if visited[o] != 1:
            return False
    left_pops = 0
    right_pops = 0
    for pa in path:
        left_pops += populations[pa - 1]
    for opa in other_path:
        right_pops += populations[opa - 1]
    result = abs(left_pops - right_pops)
    return result


# 조합 함수
def combination(N, path):
    global differ
    if path:
        # 선거구가 두 구역으로 나누어지지 않을 때는 종료
        if len(path) == N:
            return
        # 선거구가 두 구역으로 나누어진다면 bfs 함수로 연결 확인
        else:
            answer = bfs(path)
            if answer:
                if differ > answer:
                    differ = answer

    for i in range(1, N + 1):
        if i in path:
            continue

        path.append(i)
        combination(N, path)
        path.pop()


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

# 조합을 구하기 위한 path
path = []
# path 와 반대되는 다른 지역 선거구를 만들기위한 세트
reverse_path = set()
for i in range(1, N + 1):
    reverse_path.add(i)

# 두 선거구의 인구 차이의 최솟값
differ = 100 * 100

combination(N, path)

print(differ)
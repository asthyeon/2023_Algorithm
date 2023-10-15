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
import itertools


# bfs 함수
def bfs(combi, other_combi):
    global differ
    # 방문 리스트
    visited = [0] * (N + 1)
    # 큐 생성
    q = deque([combi[0]])
    # 시작점 방문 기록
    visited[combi[0]] = 1
    # 큐가 빌 때까지
    while q:
        start = q.popleft()
        for w in adj[start]:
            if visited[w] == 0 and w in combi:
                visited[w] = 1
                q.append(w)
    for c in combi:
        if visited[c] != 1:
            return False
    return bfs2(other_combi)


# bfs2 함수
def bfs2(other_combi):
    global differ
    visited2 = [0] * (N + 1)
    # 큐 생성 및 시작점 인큐
    q = deque([other_combi[0]])
    # 시작점 방문 기록
    visited2[other_combi[0]] = 1
    # 큐가 빌 때까지
    while q:
        start = q.popleft()
        for w in adj[start]:
            if visited2[w] == 0 and w in other_combi:
                visited2[w] = 1
                q.append(w)
    for o in other_combi:
        if visited2[o] != 1:
            return False
    return True


# 구역의 개수 N
N = int(input())

# 각 구역의 인구 수
populations = list(map(int, input().split()))
# 전체 인구수 합
sum_pops = sum(populations)

# 인접 리스트
adj = [[] for _ in range(N + 1)]

# 각 구역과 인접한 구역의 정보
for i in range(1, N + 1):
    # 첫 번째 정수는 인접한 구역의 수, 이후 인접한 구역의 번호
    info = list(map(int, input().split()))

    # 인접한 구역 연결
    for j in range(1, info[0] + 1):
        adj[i].append(info[j])

# path 와 반대되는 다른 지역 선거구를 만들기위한 세트
reverse_path = set()
for i in range(1, N + 1):
    reverse_path.add(i)

# 두 선거구의 인구 차이의 최솟값
differ = 100 * 100

# 인구수 차이 구하기
for j in range(1, N // 2 + 1):
    combination = list(itertools.combinations(range(1, N + 1), j))
    for combi in combination:
        left_pops = 0
        other_combi = tuple(reverse_path.difference(combi))
        for com in combi:
            left_pops += populations[com - 1]
        right_pops = sum_pops - left_pops
        result = abs(left_pops - right_pops)
        if differ > result:
            if bfs(combi, other_combi):
                differ = result


if differ == 100 * 100:
    print(-1)
else:
    print(differ)
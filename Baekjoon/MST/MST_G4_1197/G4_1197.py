import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 최소 스패닝트리의 가중치 출력
1. 최소 스패닝 트리
 - 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
@ 풀이
(1) prim 알고리즘 사용
"""
import heapq


def prim(start):
    # 힙큐
    hq = []
    # MST 에 포함되었는지 여부
    MST = [0] * V
    # 가중치 및 시작점 인큐
    heapq.heappush(hq, (0, start))
    # 누적 가중치
    total = 0
    # 큐가 빌 때까지
    while hq:
        # 가장 적은 가중치를 가진 정점 pop
        weight, v = heapq.heappop(hq)

        # 이미 방문한 정점이라면 continue
        if MST[v]:
            continue

        # 방문하지 않았다면 가중치 누적하기
        total += weight
        # 방문 체크
        MST[v] = 1

        # 갈 수 있는 정점 체크
        for new_weight, new in graph[v]:
            # 방문한 곳이라면 continue
            if MST[new]:
                continue

            # 방문하지 않았다면 인큐
            heapq.heappush(hq, (new_weight, new))
    return total




# 정점의 수 V, 간선의 수 E
V, E = map(int, input().split())

# 간선의 정보 받기
graph = [[] for _ in range(V)]
for _ in range(E):
    # 간선1 v1, 간선2 v2, 가중치 w
    v1, v2, w = map(int, input().split())

    graph[v1 - 1].append((w, v2 - 1))
    graph[v2 - 1].append((w, v1 - 1))

print(prim(0))
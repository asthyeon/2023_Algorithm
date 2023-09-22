import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 출발점은 0이다.
def djikstra(D, graph, distance):
    pq = []
    heapq.heappush(pq, (0, 0)) # 이동 거리, 출발점
    distance[0] = 0

    while pq:
        w, v = heapq.heappop(pq)
        if distance[v] < w:
            continue

        # 지름길이 없을 경우 다음 거리 그냥 방문
        if not graph[v]:
            tmp = w + 1
            if v + 1 > D: # 더 많은 거리를 간다면 종료
                continue
            if distance[v + 1] <= tmp: # 다음 위치 이미 방문했거나 더 작은값이면 pass
                continue
            distance[v + 1] = tmp
            heapq.heappush(pq, (tmp, v + 1))
        # 지름길이 있을 경우 비교
        else:
            for next in graph[v]: # (도착, 지름길 길이)
                n_w = w + next[1]
                if next[0] > D:
                    if v + 1 > D:
                        continue
                    heapq.heappush(pq, (w + 1, v + 1))
                    distance[v + 1] = w + 1
                    continue

                if distance[next[0]] <= n_w:
                    continue
                distance[next[0]] = n_w
                heapq.heappush(pq, (n_w, next[0]))
                heapq.heappush(pq, (w + 1, v + 1))

import sys
import heapq
input = sys.stdin.readline

N, D = map(int, input().split()) # 지름길 개수 N, 고속도로 길이 D
graph = [[] for i in range(D + 1)] # (도착, 지름길 길이)
INF = int(1e5)
distance = [INF] * (D + 1)
for _ in range(N):
    s, e, w = map(int, input().split()) # 시작, 도착, 지름길 길이
    if s <= D: # 시작지점이 목적지 보다 클 수 있다.
        graph[s].append((e, w))
djikstra(D, graph, distance)
print(distance[D])
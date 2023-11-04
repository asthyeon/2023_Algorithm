import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 최단 경로 길이 출력
1. 무방향 그래프
2. 1번에서 N번으로 최단 거리 이동
3. 임의로 주어진 두 정점은 반드시 통과해야 함
4. 이동했던 정점, 간선 다시 이동 가능
5. 최단 경로 없을시 -1 출력
@ 풀이
(1) 다익스트라 이용
(2) 1 에서 시작할 때, v1 에서 시작할 때, v2 에서 시작할 때 구하고
(3) 1 - v1 - v2 - N 경우, 1 - v2 - v1 - N 경우 구하기
"""
import heapq


# 다익스트라 함수
def dijkstra(adj_list, start):
    # 거리 리스트
    distances = [10e9] * (N + 1)
    # 우선순위 큐
    pq = []
    # 시작점 거리, 시작위치
    heapq.heappush(pq, (0, start))
    # 시작위치 거리 기록
    distances[start] = 0
    # 큐가 빌 때까지
    while pq:
        dist, now = heapq.heappop(pq)
        if distances[now] < dist:
            continue

        for new_dist, new in adj_list[now]:
            if distances[new] < dist + new_dist:
                continue
            distances[new] = dist + new_dist
            heapq.heappush(pq, (dist + new_dist, new))

    return distances


# 정점 수 N, 간선 수 E
N, E = map(int, input().split())
# 인접 리스트
adj_list = [[] for _ in range(N + 1)]
for _ in range(E):
    # 정점 a, b, 거리 c
    a, b, c = map(int, input().split())
    adj_list[a].append((c, b))
    adj_list[b].append((c, a))
# 반드시 거쳐야 하는 정점 v1, v2
v1, v2 = map(int, input().split())

# 1 에서 시작할 떄
start_one = dijkstra(adj_list, 1)
# v1 에서 시작할 때
start_v1 = dijkstra(adj_list, v1)
# v2 에서 시작할 때
start_v2 = dijkstra(adj_list, v2)
# v1 - v2 로 목적지를 갈 때
v1_first = start_one[v1] + start_v1[v2] + start_v2[N]
# v2 - v1 로 목적지를 갈 때
v2_first = start_one[v2] + start_v2[v1] + start_v1[N]
# 최소값 구하기
result = min(v1_first, v2_first)
if result < 10e9:
    print(result)
else:
    print(-1)


import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# i번째 줄에 i번 정점으로의 최단 경로값 출력
1. 경로가 존재하지 않는 경우 INF 출력
2. 시작점 자신은 0 출력
3. 일방향
"""
import heapq


# 다익스트라 함수
def dijkstra(K, adj):
    pq = []
    # 최단 거리 리스트
    distances = [10 * 300000] * (V + 1)
    # 시작점 인큐 및 시작점 초기화
    heapq.heappush(pq, (0, K))
    distances[K] = 0
    # 큐가 빌 때까지
    while pq:
        # 누적거리, 현재위치 디큐
        dist, now = heapq.heappop(pq)

        # 현재위치 까지 지나온 거리가 앞으로 지날 거리보다 작다면 넘기기
        if distances[now] < dist:
            continue

        # 누적 거리 및 다음위치 탐색
        for new_dist, new in adj[now]:
            # 누적 거리 = 다음 거리 +  지난 거리
            new_dist = new_dist + dist
            # 다음 위치의 누적 거리가 현재 누적 거리보다 크다면
            if distances[new] > new_dist:
                # 다음 위치의 누적 거리 교체 및 인큐
                distances[new] = new_dist
                heapq.heappush(pq, (new_dist, new))

    # 도달하지 못하는 경로가 존재한다면 INF 출력
    for i in range(1, V + 1):
        if distances[i] == 10 * 300000:
            print('INF')
        else:
            print(distances[i])


# 정점의 개수 V, 간선의 개수 E
V, E = map(int, input().split())
# 시작 정점의 번호
K = int(input())
# 간선 리스트 연결
adj = [[] for _ in range(V + 1)]
for _ in range(E):
    # u에서 v로 가는 가중치 w인 간선 존재
    u, v, w = map(int, input().split())

    adj[u].append((w, v))

# 함수 사용
dijkstra(K, adj)
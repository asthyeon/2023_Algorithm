import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 최단경로로 도달가능한 목적지들을 공백으로 분리시킨 오름차순의 정수들로 출력
1. g - h 교차로 사이에 있는 도로를 지나야함
2. s지점에서 출발해서 목적지 후보들 중 하나로 도달함
3. 양방향
4. g - h를 지나는 경우의 수가 최단경로인지 확인하고, 최단경로일 경우 도달가능한 것
@ 풀이
(1) 다익스트라 이용
(2) g, h를 지나 목적지로 도달하는 경우의 수 구하기
 - s -> 목적지1
 - s -> g -> h -> 목적지1
 - s -> h -> g -> 목적지1
 - 반복
"""
import heapq


# 다익스트라 함수
def dijkstra(start, adj_list):
    # 거리 리스트
    distances = [10000000] * (n + 1)
    # 우선순위큐
    pq = []
    # 시작거리 및 시작점 인큐
    heapq.heappush(pq, (0, start))
    # 시작점 방문처리
    distances[start] = 0

    while pq:
        dist, now = heapq.heappop(pq)

        if distances[now] < dist:
            continue

        for new_dist, new in adj_list[now]:
            new_dist = dist + new_dist
            
            # 같은 것도 넘겨야함
            if distances[new] <= new_dist:
                continue

            # 방문처리
            distances[new] = new_dist
            heapq.heappush(pq, (new_dist, new))

    return distances


T = int(input())
for tc in range(1, T + 1):
    # 교차로 수 n, 도로 수 m, 목적지 후보 수 t
    n, m, t = map(int, input().split())
    # 출발지 s, 교차로 g - h
    s, g, h = map(int, input().split())
    # 도로 정보
    adj_list = [[] for _ in range(n + 1)]
    # 도로 연결
    for _ in range(m):
        # 교차로 a, b 사이의 d 길이의 양방향 도로
        a, b, d = map(int, input().split())

        adj_list[a].append((d, b))
        adj_list[b].append((d, a))

    # 시작점에서의 거리들
    s_distances = dijkstra(s, adj_list)
    # g에서의 거리들
    g_distances = dijkstra(g, adj_list)
    # h에서의 거리들
    h_distances = dijkstra(h, adj_list)

    # s -> g -> h 경로
    g_to_h = s_distances[g] + g_distances[h]
    # s -> h -> g 경로
    h_to_g = s_distances[h] + h_distances[g]

    # 최단경로로 도달 가능한 목적지 후보
    destinations = []
    for _ in range(t):
        # 목적지
        des = int(input())

        # s -> des (실제 최단경로)
        short = s_distances[des]
        # s -> g -> h -> des 최단 경로
        g_to_h_des = g_to_h + h_distances[des]
        # s -> h -> g -> des 최단 경로
        h_to_g_des = h_to_g + g_distances[des]

        # 최단경로와 비교(둘 중 하나라도 최단경로와 같다면 도달 가능한 목적지)
        if g_to_h_des == short or h_to_g_des == short:
            destinations.append(des)

    # 목적지 후보 오름차순 정렬
    destinations.sort()

    print(*destinations)
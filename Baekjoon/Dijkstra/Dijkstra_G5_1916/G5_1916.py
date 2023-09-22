import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# A 번째 도시에서 B 번째 도시까지 가는데 드는 최소비용 출력
1. 한 도시에서 출발하여 다른 도시에 도착하는 M 개의 버스 존재
@ 풀이
(1) 다익스트라 사용
"""
import heapq


# 다익스트라 함수
def dijkstra(start, end, total_cost, buses):
    # 우선순위 큐
    pq = []
    # 출발점 에서의 비용 및 위치 인큐
    heapq.heappush(pq, (0, start))
    # 출발점 비용 갱신
    total_cost[start] = 0
    
    # 큐가 빌 때까지
    while pq:
        # 가장 작은 비용과 현재 위치 pop
        cost, now = heapq.heappop(pq)

        # 도착 도시에 도착한다면 종료
        if now == end:
            return

        # 이미 방문한 도시고 누적 비용이 현재 비용보다 더 작다면 넘기기
        if total_cost[now] < cost:
            continue

        # 현재 위치에서 갈 수 있는 도시들 비용 구하기
        for bus in buses[now]:
            n_cost = bus[0] + cost
            next = bus[1]

            # 기록된 다음 도시의 비용이 새로 소모될 비용보다 더 작거나 같다면 넘기기
            if total_cost[next] <= n_cost:
                continue

            # 새로 소모될 비용이 더 작다면 교체 후 push
            total_cost[next] = n_cost
            heapq.heappush(pq, (n_cost, next))


# 도시의 개수 N
N = int(input())
# 버스의 개수 M
M = int(input())
# 버스의 정보
buses = [[] for _ in range(N + 1)]
# 누적 비용 정보
total_cost = [100000 * 1000] * (N + 1)
# 버스의 정보 입력 받기
for _ in range(M):
    # 출발 도시번호 s, 도착 도시번호 e, 버스 비용 c
    s, e, c = map(int, input().split())
    buses[s].append((c, e))

# 구하고자 하는 출발점 start, 도착점 end
start, end = map(int, input().split())

# 함수 사용
dijkstra(start, end, total_cost, buses)

print(total_cost[end])
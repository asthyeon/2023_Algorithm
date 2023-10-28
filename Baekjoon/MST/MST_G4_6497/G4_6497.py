import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 위 조건을 지키면서 절약할 수 있는 최대 액수 구하기
1. 원래 켜져 있던 가로등 중 일부 소등하기로 함
2. 길의 가로등을 켜두면 하루에 길의 미터 수만큼 돈이 들어감
3. 불이 켜진 길로만 왕래 가능
4. 도시는 항상 연결 그래프의 형태
5. 입력의 끝에는 0, 0을 받음 => 전체를 while 문으로 구성할 것
@ 풀이
(1) prim 알고리즘
(2) MST 완성하기 -> 최소로 사용할 비용
 - 절약한 비용 = 최대 비용 - 최소로 사용할 비용
"""
import heapq


# prim 함수
def prim(now, total_cost):
    # 우선순위 큐
    pq = []
    # 방문 리스트(MST)
    MST = [0] * m
    # 시작점 push(거리, 현재위치)
    heapq.heappush(pq, (0, now))
    # 절약할 수 있는 비용
    using_cost = 0
    # 큐가 빌 때까지 반복
    while pq:
        # 디큐(거리, 현재위치)
        dist, now = heapq.heappop(pq)
        # 방문한 위치라면 컨티뉴
        if MST[now] == 1:
            continue

        # 방문 기록
        MST[now] = 1
        # 이동한 거리만큼 비용 추가
        using_cost += dist
        for cost, new in roads[now]:
            # 방문하지 않은 곳이라면 푸쉬
            if MST[new] == 0:
                heapq.heappush(pq, (cost, new))
    # 절약비용(전체비용 - 사용할 비용)
    return total_cost - using_cost


# 전체 반복
while True:
    # 집의 수 m, 길의 수 n
    m, n = map(int, input().split())
    # 종료조건을 받았을시 종료
    if m == 0 and n == 0:
        break
    # 각 길에 대한 정보
    roads = [[] for _ in range(m)]
    # 전체 비용
    total_cost = 0
    for _ in range(n):
        # 집 x번, 집 y번 사이에 z미터의 양방향 도로 존재
        x, y, z = map(int, input().split())
        roads[x].append((z, y))
        roads[y].append((z, x))
        total_cost += z

    print(prim(0, total_cost))
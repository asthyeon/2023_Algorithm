import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 목적지에 다다르기 위해 가장 빠른 시간 출력
1. a 에서 b 로 이동할 때 걸어갈 수도 있고 대포를 이용할 수 있음
2. 내린 위치에서 도착점을 향해 걸어갈 수도 있고, 또 다른 대포 이용 가능
3. 5m/s의 속도로 달림
4. 모든 대포는 당신이 원하는 임의의 방향으로 50m 날려줄 수 있음
5. 대포에 올라타고 발사되고 착륙하기까지는 정확히 2초가 걸림
6. 대포는 장애물이 아니므로 당신이 뛰는 도중에 대포가 있다면 무시하고 이동가능
@ 풀이
(1) 각 위치에서 각 대포마다의 거리를 다 구하기
(2) 다익스트라 사용
"""
import heapq
# 거리 구하는 라이브러리
import math


# 거리 구하는 함수
def distance(x1, x2, y1, y2):
    return math.hypot(x1 - x2, y1 - y2)


# 다익스트라 함수
def dijkstra(distances):
    # 누적 거리
    accumulate = [[(500 ** 2) + (500 ** 2) + 1, 0] for _ in range(n + 2)]
    # 우선순위 큐 생성
    pq = []
    # 시작거리 및 시작점, 대포 탑승 회수 인큐
    heapq.heappush(pq, (0, 0, 0))
    # 큐가 빌 때까지
    while pq:
        dist, now, cnt = heapq.heappop(pq)

        # 현재 위치를 이미 방문했고, 누적 거리보다 적게 방문했었다면 넘기기
        if accumulate[now][0] < dist:
            continue
        # 현재위치 누적거리 및 대포 탑승 회수 갱신
        accumulate[now][0] = dist
        accumulate[now][1] = cnt
        # 인접 지역 탐색
        for new_dist, new in distances[now]:
            # 다음 위치를 이미 방문했고, 누적 거리보다 적게 방문했었다면 넘기기
            if accumulate[new][0] < new_dist + dist:
                continue
            # 대포 탑승 여부 확인(2초(10m)보다 먼 거리면 대포 탑승하는게 이득)
            if new_dist > 10:
                # 누적 거리 갱신
                new_dist = new_dist + dist
                heapq.heappush(pq, (new_dist, new, cnt + 1))
            else:
                new_dist = new_dist + dist
                heapq.heappush(pq, (new_dist, new, cnt))
    
    print(accumulate)


# 현재 좌표 X, Y
start_X, start_Y = map(float, input().split())
# 목적지 좌표 X, Y
end_X, end_Y = map(float, input().split())
# 대포의 숫자 정수 n
n = int(input())
# 각 대포의 좌표
cannons = [(start_X, start_Y)]
for _ in range(n):
    x, y = map(float, input().split())
    cannons.append((x, y))
cannons.append((end_X, end_Y))
# 각 좌표의 시간 값 구하기
distances = [[] for _ in range(n + 2)]
for i in range(n + 1):
    for j in range(i + 1, n + 2):
        # 거리 구하기
        d = distance(cannons[i][0], cannons[j][0], cannons[i][1], cannons[j][1])
        # 시간 구하기, 처음일 때는 대포를 탈 수 없음
        if i == 0:
            t = d / 5
        else:
            # 시간 구하기, 거리가 30보다 크면 대포 타기
            if d > 30:
                t = 2 + (abs(d - 50) / 5)
            else:
                t = d / 5
        distances[i].append((t, j))
        distances[j].append((t, i))

print(distances)
# dijkstra(distances)















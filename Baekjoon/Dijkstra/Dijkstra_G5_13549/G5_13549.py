import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 동생을 찾는 가장 빠른 시간 찾기
1. 수빈이는 N, 동생은 K에 존재
2. 수빈이는 걷거나 순간이동 가능
 - 걷기: 1초후에 x-1 or x+1
 - 순간이동: 0초 후에 2 * X 위치로 이동
@ 풀이
(1) 다익스트라 이용
"""
import heapq


# 다익스트라 함수
def dijkstra(N, K):
    pq = []
    # 시간 리스트
    times = [10e9] * 100001
    # 시작거리 및 시작점 인큐
    heapq.heappush(pq, (0, N))
    while pq:
        time, now = heapq.heappop(pq)

        # 동생을 찾았다면 종료
        if now == K:
            print(time)
            exit()

        if times[now] != 10e9:
            continue

        # 방문 처리
        times[now] = time

        # 현재 위치가 동생을 지나쳤다면 좌측 이동만 하기
        if now > K:
            # 좌측 이동
            if now - 1 >= 0:
                    heapq.heappush(pq, (time + 1, now - 1))
                    continue

        # 좌측 이동
        if now - 1 >= 0:
            if times[now - 1] >= time + 1:
                heapq.heappush(pq, (time + 1, now - 1))

        # 우측 이동
        if now + 1 < 100001:
            if times[now + 1] >= time + 1:
                heapq.heappush(pq, (time + 1, now + 1))

        # 순간이동
        if now * 2 < 100001:
            if times[now * 2] >= time:
                heapq.heappush(pq, (time, now * 2))


# 수빈이 위치 N, 동생 위치 K
N, K = map(int, input().split())

dijkstra(N, K)


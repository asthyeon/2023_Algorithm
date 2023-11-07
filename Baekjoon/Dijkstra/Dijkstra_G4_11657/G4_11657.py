import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 1번 도시에서 출발해서 나머지 도시로 가는 가장 빠른 시간 순서대로 출력
1. M 개의 버스가 A 에서 B 로 C 시간 만큼 걸림
2. C = 0인 경우는 순간 이동, C < 0 인 경우 타임머신으로 시간을 되돌아감
3. 1번 도시에서 어떤 도시로 갈 때 타임머신을 계속 타게 된다면 -1 출력
4. 그렇지 않다면 가장 빠른 시간 순서대로 출력 및 경로 없는 도시는 -1 출력
@ 풀이
(1) 다익스트라 이용시 음수 값을 고려하지 못함
(2) 벨만-포드 알고리즘 사용
"""
import heapq
INF = 999999999999


# 다익스트라 함수
def bellman_ford(buses, distances):
    # 시작점 방문 처리
    distances[1] = 0
    # N 번의 라운드 반복
    for i in range(N):
        # 매 라운드마다 모든 버스 노선 확인
        for j in range(M):
            # 현재지점, 다음지점, 거리
            now = buses[j][0]
            new = buses[j][1]
            dist = buses[j][2]
            # 현재지점이 도달 못하는 곳이 아닐 때
            if distances[now] != INF:
                # 다음지점이 현재 지점 거리값보다 크다면 갱신
                if distances[new] > distances[now] + dist:
                    distances[new] = distances[now] + dist
                    # N 번째 라운드에서도 값이 갱신된다면 음수 순환 존재
                    if i == N - 1:
                        print(-1)
                        return

    # 음수순환이 존재하지 않는다면
    for k in range(2, N + 1):
        # 도달할 수 없다면 -1 출력
        if distances[k] == INF:
            print(-1)
        # 도달할 수 있다면 거리 출력
        else:
            print(distances[k])


# 도시의 개수 N, 버스의 개수 M
N, M = map(int, input().split())
# 최단 거리 리스트
distances = [INF] * (N + 1)
# 모든 버스 노선에 대한 정보 리스트
buses = []
for _ in range(M):
    # 시작 A, 도착 B, 거리 C
    A, B, C = map(int, input().split())
    buses.append((A, B, C))
    
bellman_ford(buses, distances)

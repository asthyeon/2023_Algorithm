import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 1번역에서 N번역으로 가는데 방문하는 최소 역의 수 구하기
1. 하이퍼튜브 하나는 역 K개를 서로 연결
2. 갈 수 없다면 -1 출력
@ 풀이
(1) 다익스트라 이용시 메모리 초과
(2) 연결정보를 튜플로 다 받아놓고 1부터 N까지 순회
"""
from collections import deque


# bfs 함수
def bfs(stations, hyper):
    # 지나온 역의 거리
    passed = [0] * (N + 1)
    # 하이퍼 튜브 이용 리스트
    used = [0] * M
    # 시작점은 1
    passed[1] = 1
    # 시작점 인큐
    q = deque([1])
    # 큐가 빌 때까지
    while q:
        start = q.popleft()
        # 시작점에 연결된 하이퍼튜브 탐색
        for j in stations[start]:
            # 방문하지 않은 하이퍼튜브라면 방문 처리
            if used[j] == 0:
                used[j] = 1
                # 하이퍼튜브 안의 역 탐색
                for k in hyper[j]:
                    # 내 자신이라면 넘기기
                    if k == start:
                        continue
                    # 방문했던 곳이라면 넘기기
                    if passed[k] != 0:
                        continue
                    passed[k] = passed[start] + 1
                    q.append(k)
                    # 목적지에 도달했다면 큐를 비우고 종료
                    if passed[N] != 0:
                        q.clear()
                        break

    if passed[-1] == 0:
        return -1
    else:
        return passed[-1]


# 역의 수 N, 역의 개수 K, 하이퍼튜브의 개수 M
N, K, M = map(int, input().split())
# 각 역이 어떤 하이퍼 튜브랑 연결되어 있는지 넣기
stations = [[] for _ in range(N + 1)]
# 하이퍼튜브 정보를 리스트에 튜플로 담기
hyper = []
for i in range(M):
    tube = tuple(map(int, input().split()))
    # 하이퍼튜브 리스트에 넣기
    hyper.append(tube)
    # 각 역이 어떤 하이퍼 튜브랑 연결되어 있는지 넣기
    for station in tube:
        stations[station].append(i)

print(bfs(stations, hyper))
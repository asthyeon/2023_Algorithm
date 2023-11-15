import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# MooTube (Silver)
[출력: Q개의 줄에 i번째 질문에 대한 K 값에 대한 추천 동영상의 개수를 대답하기]
1. 두 동영상이 얼마나 가까운 지를 측정하는 단위 "USADO"
2. N-1개의 동영상 쌍을 골라서 어떤 동영상에서 다른 동영상으로 가는 경로가 반드시 하나 존재
3. 동영상들을 네트워크 구조로 바꾸고 정점으로 나타냄
4. 값 K를 정해서 USADO가 K 이상인 모든 동영상이 추천되도록 할 것
5. 양방향 간선
@ 풀이
(1) 경로가 반드시 하나 존재 -> MST 구성
(2) 프림중독자의 프림 구현
"""
import heapq


# 프림 함수
def prim(start, adj_list):
    # 우선순위 큐 생성
    pq = []
    # 시작거리 및 시작점 인큐
    heapq.heappush(pq, (0, start))
    # 방문 리스트
    MST = [0] * (N + 1)
    # 추천 동영상 수
    videos = 0

    while pq:
        dist, now = heapq.heappop(pq)

        # 방문 여부 체크
        if MST[now]:
            continue

        MST[now] = 1

        # 다음 위치 탐색
        for new_dist, new in adj_list[now]:
            # 방문 여부 체크
            if MST[new]:
                continue

            # USADO가 K 이상이라면
            if new_dist >= k:
                # 방문하지 않은 곳인큐
                heapq.heappush(pq, (new_dist, new))
                videos += 1

    return videos


# 동영상 수 N, 농부의 질문 수 Q
N, Q = map(int, input().split())
# 간선 연결
adj_list = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    # p 와 q 가 r 값으로 이어져 있음
    p, q, r = map(int, input().split())
    
    adj_list[p].append((r, q))
    adj_list[q].append((r, p))


# 농부의 질문 Q개
for _ in range(Q):
    # USADO가 k 일 때 v 동영상을 보고 있는 소들에게 몇개의 동영상이 추천되는지
    k, v = map(int, input().split())

    print(prim(v, adj_list))












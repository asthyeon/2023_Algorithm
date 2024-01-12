import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


"""
# 숨바꼭질
1. 수빈이는 걷거나 순간이동 가능
 - 수빈이의 위치가 X일 때 걷는다면 1초후 X - 1 or X + 1로 이동
 - 순간이동한다면 1초 후에 2 * X의 위치로 이동
2. 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하기
* 입력
- N: 수빈이 위치, K: 동생 위치
[출력: 첫째 줄에 수빈이가 동생을 찾는 가장 빠른 시간, 둘째 줄에 어떻게 이동해야 하는지 출력]
"""

"""
@ 풀이
(1) 다익스트라 이용
(2) 이동한 루트를 저장해보기
(3) N이 K보다 큰 경우는 따로 만들기
"""
import heapq


# 다익스트라
def dijkstra(N, K):
    # N보다 K가 큰 경우는 뒤로 가기만 하면 되므로 새로 리스트 만들기
    if N > K:
        # 시간은 N - K, 이동 경로는 하나씩 증가하면 됨
        return N - K, [loc for loc in range(N, K - 1, -1)]
    # N이 K와 같은 경우는 바로 끝내기
    elif N == K:
        return 0, [N]

    # 힙큐 생성 및 시작점 인큐(시간, 시작점)
    hq = [(0, [N])]
    # 각 지역마다 필요한 시간 리스트
    times = [10e9] * 100001

    while hq:
        # 시간, 이동루트 디큐
        time, routes = heapq.heappop(hq)

        # 동생을 찾았다면 종료
        if routes[-1] == K:
            return time, routes

        # 방문할 지역이 시간이 더 짧은 상태로 방문했다면 넘기기
        if times[routes[-1]] <= time:
            continue

        # 방문처리
        times[routes[-1]] = time

        # 이동
        new_time = time + 1
        # 좌측 이동
        if routes[-1] > 0:
            # 시간
            new = routes[-1] - 1
            heapq.heappush(hq, (time + 1, routes + [new]))
            # 현재 위치가 동생을 지나친 상태라면 좌측 이동만
            if routes[-1] > K:
                continue

        # 우측 이동
        if routes[-1] < 100000:
            new = routes[-1] + 1
            heapq.heappush(hq, (time + 1, routes + [new]))

        # 순간이동
        if routes[-1] <= 50000:
            new = routes[-1] * 2
            heapq.heappush(hq, (time + 1, routes + [new]))


# 수빈이 위치 N, 동생 위치 K
N, K = map(int, input().split())

# 소요시간과 이동 루트 받기
spend, moved = dijkstra(N, K)

print(spend)
print(*moved)
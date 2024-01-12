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
(1) 다익스트라 이용 => 힙큐말고 덱 사용(bfs)
(2) 이동한 루트를 저장해보기 => q에 저장하면 시간초과
(3) 하나의 루트에 이동 경로를 저장하고 추적하는 방식으로 해보기
"""
from collections import deque


# bfs
def bfs(N, K):
    # 힙큐 생성 및 시작점 인큐(시간, 시작점)
    pq = deque([(0, N)])
    # 각 지역마다 필요한 시간 리스트
    times = [10e9] * 100001

    while pq:
        # 시간, 현재 위치 디큐
        time, now = pq.popleft()

        # 동생을 찾았다면 종료
        if now == K:
            answer = moved(time, now)
            return time, answer

        # 이동
        new_time = time + 1
        # 좌측 이동
        if now - 1 >= 0:
            new = now - 1
            # 방문하지 않았다면
            if times[new] == 10e9:
                times[new] = new_time
                # 이전 위치 저장
                passed[new] = now
                pq.append((new_time, new))
                # 현재 위치가 동생을 지나친 상태라면 좌측 이동만
                if now > K:
                    continue

        # 우측 이동
        if now + 1 < 100001:
            new = now + 1
            # 방문하지 않았다면
            if times[new] == 10e9:
                times[new] = new_time
                # 이전 위치 저장
                passed[new] = now
                pq.append((new_time, new))

        # 순간이동
        if now * 2 <= 100001:
            new = now * 2
            # 방문하지 않았다면
            if times[new] == 10e9:
                times[new] = new_time
                # 이전 위치 저장
                passed[new] = now
                pq.append((new_time, new))


# 이동 경로 찾기
def moved(time, location):
    # 이동경로를 저장할 리스트
    path = []
    # 소요된 시간만큼 경로 저장
    for _ in range(time + 1):
        # 위치 저장
        path.append(location)
        # 위치 저장 후 어디서 왔는지 뒤로 가기
        location = passed[location]
    
    # 방향을 바꿔서 반환
    return path[::-1]


# 수빈이 위치 N, 동생 위치 K
N, K = map(int, input().split())

# 이동 경로를 저장할 리스트
passed = [-1] * 100001
# 소요시간 및 경로 받기
spend, answer = bfs(N, K)

print(spend)
print(*answer)




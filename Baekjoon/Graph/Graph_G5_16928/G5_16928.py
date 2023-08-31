import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
from collections import deque

"""
# 주사위를 굴리는 최솟값
1. 사다리는 올라가고, 뱀은 내려간다
2. 뱀만 만나기
3. 2차원 배열이 아닌 1차원 배열
@ 풀이
1. bfs로 모든 경우의 수 만들기
"""


# bfs 함수
def bfs(sx):
    # 방문 리스트
    visited = [0] * 101
    # 시작점 인큐
    q = deque([sx])
    # 시작점 방문 체크
    visited[sx] = 1
    # 큐가 빌 때까지
    while q:
        # 디큐
        sx = q.popleft()
        # 주사위 탐색
        for i in range(1, 7):
            nx = sx + i
            # 도착
            if nx == 100:
                visited[nx] = visited[sx] + 1
                q.clear()
                break
            # 방문한 곳이면 바로 건너뛰기
            if visited[nx] != 0:
                continue
            # 사다리 혹은 뱀을 만났을 때(반복 가능)
            if ladder[nx] > 0:
                if visited[nx] == 0:
                    mx = nx
                    # 연속으로 만났을 때도 고려하기
                    while ladder[mx] != 0:
                        # 뱀인 경우 도착지에서 방문 체크 X
                        if mx > ladder[mx]:
                            if visited[mx] == 0:
                                q.append(ladder[mx])
                                visited[mx] = visited[sx] + 1
                                if visited[ladder[mx]] == 0:
                                    visited[ladder[mx]] = visited[sx] + 1
                                mx = ladder[mx]
                            else:
                                break
                        # 사다리인 경우
                        else:
                            if visited[mx] == 0:
                                q.append(ladder[mx])
                                visited[mx] = visited[sx] + 1
                                if visited[ladder[mx]] == 0:
                                    visited[ladder[mx]] = visited[sx] + 1
                                mx = ladder[mx]
                            else:
                                break
            # 그냥 전진할 때
            else:
                if visited[nx] == 0:
                    q.append(arr[nx])
                    visited[nx] = visited[sx] + 1
    return visited[100] - 1


# 사다리 수: N, 뱀의 수: M
N, M = map(int, input().split())
# 보드판 형성
arr = [i for i in range(101)]
# 사다리, 뱀 입력판
ladder = [0] * 101


# 사다리 입력
for _ in range(N):
    l1, l2 = map(int, input().split())
    ladder[l1] = l2
# 뱀 입력
for _ in range(M):
    s1, s2 = map(int, input().split())
    ladder[s1] = s2

print(bfs(1))


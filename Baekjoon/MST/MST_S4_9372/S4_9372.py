import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 비행 스케줄이 주어질 때 가장 적은 종류의 비행기를 타는 수
1. 다른 국가로 이동할 때 다른 국가를 거쳐가도 괜찮음
@ 풀이
(1) dfs 사용
"""


# dfs 함수
def dfs(start):
    # 방문 리스트
    visited = [0] * N
    # 스택 생성
    stack = []
    # 시작점 방문체크
    visited[start] = 1
    # 비행기 탑승수
    plane = 0
    # q가 빌 때까지
    while True:
        # 인접지역 탐색
        for n in adj[start]:
            # 방문하지 않은 곳이라면 방문하기
            if visited[n] == 0:
                stack.append(start)
                visited[n] = visited[start] + 1
                start = n
                plane += 1
                break
        # 인접지역을 다 탐색했다면 이전으로 돌아가거나 종료
        else:
            # 돌아갈 곳이 남았다면 돌아가기
            if stack:
                start = stack.pop()
            # 돌아갈 곳이 없다면 종료
            else:
                break
    return plane


T = int(input())
for tc in range(1, T + 1):
    # 국가의 수 N, 비행기의 종류 M
    N, M = map(int, input().split())
    # 인접리스트
    adj = [[] * N for _ in range(N)]
    # 국가간 비행기 연결
    for _ in range(M):
        m1, m2 = map(int, input().split())

        adj[m1 - 1].append(m2 - 1)
        adj[m2 - 1].append(m1 - 1)

    print(dfs(0))
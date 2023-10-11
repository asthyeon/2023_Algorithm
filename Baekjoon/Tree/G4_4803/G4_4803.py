import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 그래프가 주어졌을 때 트리의 개수를 세기
1. 연결 요소는 모든 정점이 서로 연결되어 있는 정점의 부분집합
2. 그래프는 하나 이상의 연결 요소로 이루어짐
3. 트리는 사이클이 없는 연결 요소
4. 트리의 성질
 - 정점이 n개
 - 간선이 n-1개
 - 임의의 두 정점에 대해서 경로가 유일함
5. 입력은 여러 개의 테스트 케이스로 이루어져 있음
6. 입력의 마지막 줄에는 0이 2개 주어짐
7. 출력조건: 다음 내용을 테스트 케이스 번호와 함께 출력
 - 트리 X: Case 1: No trees.
 - 트리 1개: Case 2: There is on tree.
 - 트리 T개: Case 3: A forest of T trees.
8. 무방향
@ 풀이
(1) 정점을 다 연결
(2) bfs 를 통해서 트리인지 확인
 - 사이클이 있다면(다시 돌아오는 길이 있다면 트리 X)
"""
from collections import deque


# bfs 함수
def bfs(start, visited, n, adj):
    global T
    # 트리 조건
    tree = True
    # 지나온 길
    passed = [0] * (n + 1)
    # 큐 생성 및 시작점 인큐
    q = deque([start])
    # 시작점 방문 기록
    visited[start] = 1
    # 큐가 빌 때까지
    while q:
        # 지나온 길 기록
        passed[start] = 1
        # 디큐
        start = q.popleft()
        for w in range(n + 1):
            # 인접할 때
            if adj[start][w] == 1:
                # 방문하지 않았다면
                if visited[w] == 0:
                    # 방문 기록
                    visited[w] = 1
                    # 인큐
                    q.append(w)
                # 방문한 곳이라면
                else:
                    # 지나온 길이라면 넘기기
                    if passed[w] == 1:
                        continue
                    # 지나온 길이 아니라면 트리 X
                    else:
                        tree = False
    # 트리라면 개수 + 1
    if tree:
        T += 1
        return


# 케이스 번호
case = 0
while True:
    case += 1
    # 정점의 개수 n, 간선의 개수 m
    n, m = map(int, input().split())

    # 종료조건
    if n == 0 and m == 0:
        break

    # 인접 행렬
    adj = [[0] * (n + 1) for _ in range(n + 1)]

    # 간선 연결
    for _ in range(m):
        v1, v2 = map(int, input().split())

        adj[v1][v2] = 1
        adj[v2][v1] = 1

    # 방문 리스트
    visited = [0] * (n + 1)

    # 트리의 개수
    T = 0

    # 트리 개수 세기
    for i in range(1, n + 1):
        # 방문하지 않았다면 bfs 돌기
        if visited[i] != 1:
            bfs(i, visited, n, adj)

    # 케이스 번호
    print(f'Case {case}:', end=' ')
    if T == 0:
        print('No trees.')
    elif T == 1:
        print('There is one tree.')
    else:
        print(f'A forest of {T} trees.')

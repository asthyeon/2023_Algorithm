import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 회장의 점수와 회장이 될 수 있는 모든 사람 찾기
1. 어느 회원이 다른 모든 회원과 친구이면 이 회원 점수는 1점
2. 어느 회원의 점수가 2점이면, 다른 모든 회원이 친구이거나 친구의 친구임
3. 어느 회원의 점수가 3점이면, 다른 모든 회원이 친구이거나, 친구의 친구이거나, 친구의 친구의 친구임
4. 주의할 점은 어떤 두 회원이 친구사이이면서 동시에 친구의 친구사이이면 이 두사람은 친구사이
5. 회장은 회원들 중에서 점수가 가장 작은 사람
@ 풀이
(1) 자기랑 가장 먼 사이가 점수가 됨
 - 1번: 5번과 친구의 친구의 친구 = 3점
 - 2번: 5번과 친구의 친구 = 2점
 - 3번: 1번과 친구의 친구 = 2점
 - 4번: 1번과 친구의 친구 = 2점
 - 5번: 1번과 친구의 친구의 친구 = 3점
(2) bfs로 탐색횟수 세기
 - 탐색횟수 = 점수
"""
from collections import deque


# bfs 함수
def bfs(friends, start):
    # 방문 리스트
    visited = [-1] * (N + 1)
    # 큐 생성 및 거리 및 시작점 인큐
    q = deque([(0, start)])
    # 시작점 방문 기록
    visited[start] = 1
    # 큐가 빌 때까지
    while q:
        dist, now = q.popleft()
        # 인접한 사이 중에
        for new in friends[now]:
            # 방문하지 않았다면
            if visited[new] == -1:
                # 인큐
                q.append((dist + 1, new))
                # 방문 기록(거리 값으로 방문 기록하기
                visited[new] = dist + 1

    # 제일 큰 점수 반환
    return max(visited)


# 회원의 수
N = int(input())
# 친구 사이 리스트
friends = [[] for _ in range(N + 1)]
while True:
    member1, member2 = map(int, input().split())
    if member1 == -1 and member2 == -1:
        break
    friends[member1].append(member2)
    friends[member2].append(member1)

# 멤버들의 점수 리스트
scores = [100] * (N + 1)
# 점수 할당
for i in range(1, N + 1):
    score = bfs(friends, i)
    scores[i] = score

# 회장 점수, 후보 그리고 후보 수 구하기(맨 앞 0 제거)
president_score = min(scores)
candidates = []
cnt = 0
for j in range(1, N + 1):
    # 후보의 점수가 회장 점수라면 후보 리스트에 넣기
    if scores[j] == president_score:
        candidates.append(j)
        cnt += 1

# 회장 점수 및 후보 수 출력
print(president_score, cnt)
# 후보 출력
print(*candidates)
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 마라톤 2
[출력:
1. 모든 체크포인트를 순서대로 방문해야 함
2. 체크포인트를 최대 K개 건너뛰면서 달릴 수 있음
3. 1번, N번은 건너뛰지 않음
4. 택시거리 사용 (x1, y1)과 (x2, y2) 점 간의 거리: |x1 - x2| + |y1 - y2|
5. 체크포인트의 좌표는 겹칠 수도 있음(건너뛸 때도 한 겹친 것 하나만 건너뜀)
@ 풀이
(1) 마라톤 1처럼 풀어보기
(2) 모든 체크포인트 사이 거리 구해놓기
(3) 2차원 배열 dp로 풀어보기
- dp[K][N]
(4) 스킵횟수에 따라 값을 지정
0번 거리 [0, 2, 2, 5, 3, 3]
1번 거리 [2, 0, 2, 5, 5, 3]
2번 거리 [2, 2, 0, 7, 3, 5]
3번 거리 [5, 5, 7, 0, 4, 4]
4번 거리 [3, 5, 3, 4, 0, 6]
5번 거리 [3, 3, 5, 4, 6, 0]

1번 생략: 2, 7, 4, 6 = 19
2번 생략: 2, 5, 4, 6 = 17
3번 생략: 2, 2, 3, 6 = 13
4번 생략: 2, 2, 7, 4 = 15

0 -> 2번 = 4
2, 2
1번 생략 = 2
2

0 -> 3번 = 11
2, 2, 7
1번 생략 = 9
2, 7
2번 생략 = 7
2, 5

0 -> 4번 = 15
2, 2, 7, 4
1번 생략 = 13
2, 7, 4
2번 생략 = 10
2, 5, 3
3번 생략 = 7
2, 2, 3
"""
# 최대값 설정
INF = 10e9


# dp 함수
def dynamic_programming(checkpoints, distances):
    dp = [[INF] * N for _ in range(K + 1)]

    for k in range(K + 1):
        for n in range(1, N):
            # 스킵이 없을 때
            if k == 0:
                # 처음 값은 0으로 고정
                dp[k][0] = 0
                # 이전 값에 현재 거리 값을 더하기
                dp[k][n] = dp[k][n - 1] + distances[n - 1][n]
            # 스킵이 있을 때
            else:
                if n == 1:
                    # 처음 값은 0으로 고정
                    dp[k][n - 1] = 0
                    # 첫번째 체크포인트는 스킵 불가능
                    dp[k][n] = distances[0][n]
                else:
                    # 스킵횟수에 따른 계산
                    for skip in range(k + 1):
                        # 스킵한 지점이 0보다 크거나 같을 때
                        if n - skip - 1 >= 0:
                            # print(f'스킵횟수: {skip} 가야할 위치: {n}')
                            # print(f'현재값: {dp[k][n]}, 값: {dp[k - skip][n - skip - 1]} + {distances[n][n - skip - 1]}, 값2: {dp[k][n - 1]} + {distances[n - 1][n]}')
                            # 현재값, 스킵을 한 지점 + 현재까지의 거리, 직전 지점 + 직전지점에서의 거리 중 최소값으로 교체
                            dp[k][n] = min(dp[k][n],
                                           dp[k - skip][n - skip - 1] + distances[n - skip - 1][n],
                                           dp[k][n - 1] + distances[n - 1][n])
                            # print(f'선택된 값: {dp[k][n]}')
    # 마지막 도착값 반환
    return dp[-1][-1]


# 전체 체크포인트 수 N, 건너뛸 체크포인트 수 K
N, K = map(int, input().split())
# 체크포인트 좌표
checkpoints = []
for _ in range(N):
    x, y = map(int, input().split())
    checkpoints.append((x, y))

# 모든 체크포인트들 사이의 거리를 구해놓기
distances = [[0] * N for _ in range(N)]
for i in range(N - 1):
    for j in range(i + 1, N):
        dist = abs(checkpoints[i][0] - checkpoints[j][0]) + abs(checkpoints[i][1] - checkpoints[j][1])
        distances[i][j] = dist
        distances[j][i] = dist

# for _ in range(N):
#     print(f'{_}번 거리 {distances[_]}')
print(dynamic_programming(checkpoints, distances))
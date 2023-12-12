import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 우유 도시
[출력: 마실 수 있는 우유의 최대 개수]
1. 우유 마시는 규칙
 - 맨 처음에는 딸기우유 한 팩
 - 딸기우유 다음 초코우유
 - 초코우유 다음 바나나우유
 - 바나나우유 다음 딸기우유
2. 영학이는 (1, 1)에서 출발해 (N, N)까지 가면서 우유를 사 마심
3. 영학이가 마실 수 있는 최대 우유 개수 구하기
4. 0: 딸기우유, 1: 초코우유, 2: 바나나우유
5. 오직 동쪽 또는 남쪽으로만 움직이고 우유를 마실 수도 안마실 수도 있음
@ 풀이
(1) bfs로 마시는 경우 안마시는 경우 둘 다 체크 => 메모리 초과
(2) dp로 풀기
 - dp 값은 그 지점까지 우유를 마신 최대 개수 => 우유를 마신상태를 기억 못함
 - dp 값에 어떤 우유를 마셨는지 상태 값도 같이 넣기
 - 꼭 0, 0 에서 우유를 마시지 않아도 됨
"""
# 다음 우유 좌표(처음에 우유를 안마셨을 때를 위해 -1 넣기)
milk = {-1: 0, 0: 1, 1: 2, 2: 0}


# dp 함수
def dynamic_programming(city):
    dp = [[(-1, 0)] * N for _ in range(N)]

    for x in range(N):
        for y in range(N):
            # 첫번째 행일 때
            if x == 0:
                # 우유를 마실 수 있는지 확인
                if city[x][y] == milk[dp[x][y - 1][0]]:
                    # 우유를 마시고 넘어갈 수 있으면 마시기
                    dp[x][y] = (milk[dp[x][y - 1][0]], dp[x][y - 1][1] + 1)
                else:
                    dp[x][y] = (dp[x][y - 1][0], dp[x][y - 1][1])
            # 첫번째 열일 때
            elif y == 0:
                # 우유를 마실 수 있는지 확인
                if city[x][y] == milk[dp[x - 1][y][0]]:
                    # 우유를 마시고 넘어갈 수 있으면 마시기
                    dp[x][y] = (milk[dp[x - 1][y][0]], dp[x - 1][y][1] + 1)
                else:
                    # 우유를 마실 수 없으면 마시지 않기
                    dp[x][y] = (dp[x - 1][y][0], dp[x - 1][y][1])
            # 그 외일 때
            else:
                # 위에서 우유를 마실 수 있는지 확인
                if city[x][y] == milk[dp[x - 1][y][0]]:
                    up_milk = milk[dp[x - 1][y][0]]
                    up_drink = dp[x - 1][y][1] + 1
                else:
                    up_milk = dp[x - 1][y][0]
                    up_drink = dp[x - 1][y][1]
                # 왼쪽에서 우유를 마실 수 있는지 확인
                if city[x][y] == milk[dp[x][y - 1][0]]:
                    left_milk = milk[dp[x][y - 1][0]]
                    left_drink = dp[x][y - 1][1] + 1
                else:
                    left_milk = dp[x][y - 1][0]
                    left_drink = dp[x][y - 1][1]
                # 더 큰 값으로 교체
                if up_drink > left_drink:
                    dp[x][y] = (up_milk, up_drink)
                else:
                    dp[x][y] = (left_milk, left_drink)

    # for _ in range(N):
    #     print(dp[_])

    # N, N에 도착했을 때 최대 개수 반환
    return dp[-1][-1][1]


# 우유 도시 크기 N
N = int(input())
# 우유 도시 정보
city = [list(map(int, input().split())) for _ in range(N)]

print(dynamic_programming(city))
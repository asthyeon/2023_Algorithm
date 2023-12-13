import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 최고의 팀 만들기
[출력: 만들 수 있는 팀 중 가장 큰 능력치를 갖는 팀의 능력치 출력]
1. 흑 플레이 15명, 백 플레이 15명
2. 흑, 백의 능력치는 1 ~ 100
3. 팀 전체 능력치는 흑 전체 능력치 + 백 전체 능력치
4. 플레이어 한명의 백 능력치, 흑 능력치가 주어짐
5. 해당 능력치를 토대로 가장 큰 능력치를 갖는 팀 능력치 출력
@ 풀이
(1) 그냥 풀어보기
(2) 우선순위 큐 이용 => 같을 때 처리를 못하겠음
(3) dp 이용
 - dp[p][w][b] = 현재까지의 능력치들의 합 중 최대값
 - p: 해당 번호 선수
 - w: 백 플레이어일 때
 - b: 흑 플레이어일 때
 
"""
# 선수정보
players = []


# dp 함수
def dynamic_programming(players):
    dp = [[[0] * 16 for _ in range(16)] for _ in range(len(players) + 1)]
    
    # 선수 수만큼 반복
    for p in range(len(players)):
        # 백 플레이어가 15번이 될 때까지 반복
        for w in range(16):
            # 흑 플레이어가 15번이 될 때까지 반복
            for b in range(16):
                # 백 플레이어가 15번 전이라면
                if w < 15:
                    # 해당 선수를 백 플레이어로 쓰지 않을 때와 쓸 때를 비교
                    dp[p + 1][w + 1][b] = max(dp[p + 1][w + 1][b], dp[p][w][b] + players[p][0])
                # 흑 플레이어가 15번 전이라면
                if b < 15:
                    # 해당 선수를 백 플레이어로 쓰지 않을 때와 쓸 때를 비교
                    dp[p + 1][w][b + 1] = max(dp[p + 1][w][b + 1], dp[p][w][b] + players[p][1])
                # 해당 번호를 그 선수를 쓸 때와 안 쓸 때중 큰 값으로 지정
                dp[p + 1][w][b] = max(dp[p + 1][w][b], dp[p][w][b])

    return dp[len(players)][-1][-1]


while True:
    # 입력이 있을 때
    try:
        # 백 능력치, 흑 능력치
        white, black = map(int, input().split())
        # 선수정보에 넣기
        players.append((white, black))

    # 입력이 없으면 결과 출력 후 반복 종료
    except:
        print(dynamic_programming(players))
        break

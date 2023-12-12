import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 파일 합치기
[출력: 테스트 케이스마다 모든 장을 필요하는데 필요한 최소 비용 출력]
1. 여러 파일을 하나로 합치기
2. 두 파일을 합칠 때 필요한 비용이 두 파일 크기의 합
3. 한 개의 파일을 완성하는데 필요한 비용의 총 합 구하기
4. 파일을 합치는 순서를 조정 가능
@ 풀이
(1) dp 이용
(2) 누적합 이용하기
K = [40, 30, 30, 50]
S = [40, 70, 100, 150]

   0   1   2   3
0  0   70  160 300
1  0   0   60  170
2  0   0   0   80
3  0   0   0   0
 
dp[0][1] = 0번 + 1번
dp[1][2] = 1번 + 2번
dp[2][3] = 2번 + 3번

dp[0][2] = 0 ~ 2번 누적합 + min(dp[0][1], dp[1][2])
dp[1][3] = 1 ~ 3번 누적합 + min(dp[1][2], dp[2][3])

dp[0][3] = 1 ~ 4번 누적합 + min(dp[0][2], dp[1][3])
"""


# dp 함수
def dynamic_programming(files):
    dp = [[0] * K for _ in range(K)]
    
    # 가로 행은 역순
    for i in range(K - 1, -1, -1):
        # 세로 열은 정방향
        for j in range(i + 1, K):
            # 2개를 합칠 때
            if dp[i + 1][j] == 0 and dp[i][j - 1] == 0:
                dp[i][j] = files[i] + files[j]
            # 3개 이상을 합칠 때
            else:
                # 이전값들 중 최소값 찾기
                min_list = set()
                for k in range(i, j):
                    min_list.add(dp[i][k] + dp[k + 1][j])
                dp[i][j] = min(min_list)
                # + 누적합
                if i - 1 < 0:
                    dp[i][j] += S[j]
                else:
                    dp[i][j] += S[j] - S[i - 1]

    return dp[0][-1]


T = int(input())
for tc in range(1, T + 1):
    # 소설 장 수 K
    K = int(input())
    # 각 소설 파일의 크기
    files = list(map(int, input().split()))

    # 누적합 구하기
    S = [files[0]]
    for k in range(K - 1):
        S.append(S[k] + files[k + 1])

    print(dynamic_programming(files))
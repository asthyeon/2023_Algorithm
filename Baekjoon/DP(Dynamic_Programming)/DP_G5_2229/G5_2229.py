import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 학생들의 점수가 주어졌을 때 조가 잘 짜여진 정도의 최댓값 구하기
1. 학생들을 나이 순서대로 우선 정렬
2. 적당히 학생들을 나누기(조의 개수는 상관 X)
3. 각각의 조가 잘 짜여진 정도: 그 조에 속한 가장 점수가 높은 학생의 점수 - 가장 점수가 낮은 학생의 점수
4. 전체적으로 조가 잘 짜여진 정도: 각각의 조가 잘 짜여진 정도의 합
5. 한 명으로 조가 구성되는 경우 그 조의 잘 짜여진 정도: 0(가장 높은 점수 = 가장 낮은 점수)
@ 풀이
(1) dp로 풀기
    - dp[0] = 0 (scores[0] - scores[0])
    - dp[1] = 3 (max(scores[0:2]) - min(scores[0:2]))
    - dp[2] = 5 max(
                max(scores[0:3]) - min(scores[0:3],
                dp[0] + (max(scores[1:3]) - min(scores[1:3])),
                dp[1] + 0
                )
    - dp[3] = 9 max(
                max(scores[0:4]) - min(scores[0:4],
                dp[0] + (max(scores[1:4]) - min(scores[1:4])),
                dp[1] + (max(scores[2:4]) - min(scores[2:4])),
                dp[2] + 0
                )
    - dp[4] = 6 max(
                max(scores[0:5]) - min(scores[0:5],
                dp[0] + (max(scores[1:5]) - min(scores[1:5])),
                dp[1] + (max(scores[2:5]) - min(scores[2:5]))
                dp[2] + (max(scores[3:5]) - min(scores[3:5])),
                dp[3] + (max(scores[4:5]) - min(scores[4:5])) = dp[3],
                )                
"""


# dp 함수
def dynamic_programming(scores):
    dp = [0] * N
    for i in range(1, N):
        for j in range(i):
            dp[i] = max(dp[i], dp[j - 1] + max(scores[j:i + 1]) - min(scores[j:i + 1]))

    return dp[-1]


# 학생 수 N
N = int(input())
# 학생들의 점수(나이순)
scores = list(map(int, input().split()))

print(dynamic_programming(scores))
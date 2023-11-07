import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 모두의 부분수열이 되는 수열 중 가잔 긴 것을 찾기
1. LCS: 최장 공통 부분 수열
2. 첫째 줄에 LCS의 길이, 둘째 줄에 LCS 출력
@ 풀이
(1) dp로 풀어보기

ACAYKP
CAPCAK
 -     A C A Y K P
     0 0 0 0 0 0 0
   C 0 0 1 1 1 1 1
   A 0 1 1 2 2 2 2
   P 0 1 1 2 2 2 3
   C 0 1 2 2 2 2 3
   A 0 1 2 3 3 3 3
   K 0 1 2 3 3 4 4

ABCDEF
BEFDEFACDFABZ
 -     A B C D E F
     0 0 0 0 0 0 0
   B 0 0 1 1 1 1 1
   E 0 0 1 1 1 2 2
   F 0 0 1 1 1 2 3
   D 0 0 1 1 2 2 3
   E 0 0 1 1 2 3 3
   F 0 0 1 1 2 3 4
   A 0 1 1 1 2 3 4
   C 0 1 1 2 2 3 4
   D 0 1 1 2 3 3 4
   F 0 1 1 2 3 3 4
   A 0 1 1 2 3 3 4
   B 0 1 2 2 3 3 4
   Z 0 1 2 2 3 3 4

CCCBBBACA
AAACCCABA
 -     C C C B B B A C A
     0 0 0 0 0 0 0 0 0 0
   A 0 0 0 0 0 0 0 1 1 1
   A 0 0 0 0 0 0 0 1 1 2
   A 0 0 0 0 0 0 0 1 1 2
   C 0 1 1 1 1 1 1 1 2 2
   C 0 1 2 2 2 2 2 2 2 2
   C 0 1 2 3 3 3 3 3 3 3
   A 0 1 2 3 3 3 3 4 4 4
   B 0 1 2 3 4 4 4 4 4 4
   A 0 1 2 3 4 4 4 5 5 5

ADQWEQWDQWGFSDAHWREYERFGD
FGDGFDSGWERDSAFLSD

        A D Q W E Q W D Q W G F S D A H W R E Y E R F G D
      0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
    F 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1
    G 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2
    D 0 0 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 3
    G 0 0 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2 2 2 3 3
    F 0 0 1 1 1 1 1 1 1 1 1 2 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    D 0 0 1 1 1 1 1 1 2 2 2 2 3 3 4 4 4 4 4 4 4 4 4 4 4 4
    S 0 0 1 1 1 1 1 1 2 2 2 2 3 4 4 4 4 4 4 4 4 4 4 4 4 4
    G 0 0 1 1 1 1 1 1 2 2 2 3 3 4 4 4 4 4 4 4 4 4 4 4 5 5
    W 0 0 1 1 2 2 2 2 2 2 3 3 3 4 4 4 4 5 5 5 5 5 5 5 5 5
    E 0 0 1 1 2 3 3 3 3 3 3 3 3 4 4 4 4 5 5 6 6 6 6 6 6 6
    R 0 0 1 1 2 3 3 3 3 3 3 3 3 4 4 4 4 5 6 6 6 6 7 7 7 7
    D 0 0 1 1 2 3 3 3 4 4 4 4 4 4 5 5 5 5 6 6 6 6 7 7 7 8
    S 0 0 1 1 2 3 3 3 4 4 4 4 4 5 5 5 5 5 6 6 6 6 7 7 7 8
    A 0 1 1 1 2 3 3 3 4 4 4 4 4 5 5 6 6 6 6 6 6 6 7 7 7 8
    F 0 1 1 1 2 3 3 3 4 4 4 4 5 5 5 6 6 6 6 6 6 6 7 8 8 8
    L 0 1 1 1 2 3 3 3 4 4 4 4 5 5 5 6 6 6 6 6 6 6 7 8 8 8
    S 0 1 1 1 2 3 3 3 4 4 4 4 5 6 6 6 6 6 6 6 6 6 7 8 8 8
    D 0 1 2 2 2 3 3 3 4 4 4 4 5 6 7 7 7 7 7 7 7 7 7 8 8 9

(2) 두 문자가 같다면 dp[x][y] = dp[x - 1][y - 1] + 1
(3) 두 문자가 다르다면 위쪽과 왼쪽 중 큰 값 dp[x][y] = max(dp[x - 1][y], dp[x][y - 1]) 
"""


# dp 함수
def dynamic_programming(word1, word2):
    dp = [[0] * (len(word1) + 1) for _ in range(len(word2) + 1)]

    # dp 탐색
    for x in range(1, len(word2) + 1):
        for y in range(1, len(word1) + 1):
            # 두 문자가 같다면
            if word2[x - 1] == word1[y - 1]:
                dp[x][y] = dp[x - 1][y - 1] + 1
            # 두 문자가 다르다면
            else:
                dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])

    # 역추적으로 LCS 만들기
    LCS = ''
    x_line = len(word2)
    y_line = len(word1)
    while x_line != 0 and y_line != 0:
        # 같은 수를 찾기
        # 왼쪽 위와 비교
        if dp[x_line][y_line] == dp[x_line - 1][y_line - 1]:
            x_line -= 1
            y_line -= 1
            continue
        # 왼쪽과 비교
        elif dp[x_line][y_line] == dp[x_line][y_line - 1]:
            y_line -= 1
            continue
        # 위쪽과 비교
        elif dp[x_line][y_line] == dp[x_line - 1][y_line]:
            x_line -= 1
            continue
        # 같은 수가 없다면 해당 문자 LCS에 넣은 후 왼쪽 위로 이동
        else:
            LCS = word1[y_line - 1] + LCS
            x_line -= 1
            y_line -= 1

    # 문자열의 길이 및 문자열 출력
    if LCS == '':
        return len(LCS)
    else:
        return len(LCS), LCS


# 두 문자열 입력
word1 = input().rstrip()
word2 = input().rstrip()

answers = dynamic_programming(word1, word2)
# LCS의 길이에 따라 출력 조건 다르게하기
if answers == 0:
    print(answers)
else:
    print(answers[0])
    print(answers[1])


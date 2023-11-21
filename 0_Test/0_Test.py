import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 로마 숫자 만들기
[출력: 로마 숫자 N개를 사용해서 만들 수 있는 서로 다른 수의 개수 출력]
1. 로마 숫자 I, V, X, L (1, 5, 10, 50)
2. XXXV = 35, IXI = 12
3. 순서 상관X
4. 로마 숫자 N개를 사용해서 만들 수 있는 서로 다른 수의 개수 구하기
@ 풀이
(1) 직접 해보기
N = 1
 I V X L
전체: 4
중복: 0
개수: 4

N = 2
 II (IV) (IX) (IL)
 VI  VV  (VX) (VL) 
 XI  XV   XX  (XL) 
 LI  LV   LX   LL
전체: 16
중복: 6
개수: 10

N = 3
 [2]  [6]   [11]  [51]   [6]   [10]  [15]  [55]   [11]  [15]  [20]  [60]   [51]  [55]  [60]  [100]
 III (IIV) (IIX) (IIL)  (IVI) (IVV) (IVX) (IVL)  (IXI) (IXV) (IXX) (IXL)  (ILI) (ILV) (ILX) (ILL) [1]
 3    (7)  (12) (52)     (7)  (11) (16) (56)  (12) (16) (21) (61)     (52) (56) (61) (101)
 
 3 - 1개
 
 VII  VIV  (VIX) (VIL)   VVI   VVV  (VVX) (VVL)  (VXI) (VXV) (VXX) (VXL)  (VLI) (VLV) (VLX) (VLL) [5]
 7    11    (16) (56)     (11) 15 (20) (60)     (16) (20) (25) (65)     (56) (60) (65) (105)
 
 7 11 15 - 3개  
 
 XII  XIV   XIX  (XIL)   XVI   XVV   XVX  (XVL)   XXI   XXV   XXX  (XXL)  (XLI) (XLV) (XLX) (XLL) [10]
 12   16    21   (61)     (16) 20 25 (65)     (21) (25) 30 (70)     (61) (65) (70) (110)
 
 12 16 21 20 25 30 - 6개
 
 LII  LIV   LIX   LIL    LVI   LVV   LVX   LVL    LXI   LXV   LXX   LXL    LLI   LLV   LLX   LLL  [50]
 52   56    61    101    (56)    60    65    105    (61)    (65)    70    110    (101)   (105)   (110)   150
 
 52 56 61 101 60 65 105 70 110 150 - 10개
 
전체: 64
중복: 44
개수: 20

(2) 규칙 찾기
1 1  1  1   [4]
1 2  3  4   [10]
1 3  6  10  [20]
1 4  10 20  [35]
1 5  15 35  [56]
1 6  20 56  [83]
1 7  25 83  [116]
1 8  30 116 [155]
1 9  33 155 [198]
1 10 35 198 [244]
(3) dp로 풀기
"""


# dp 함수
def dynamic_programming(N):
    dp = [[0] * 4 for _ in range(N)]
    dp[0][0] = 1
    dp[0][1] = 1
    dp[0][2] = 1
    dp[0][3] = 1

    for i in range(1, N):
        dp[i][0] = 1
        dp[i][1] = dp[i - 1][1] + 1
        dp[i][2] = dp[i - 1][2] + dp[i][1]
        dp[i][3] = sum(dp[i - 1])

    for _ in range(N):
        print(dp[_])


# 사용할 수 있는 문자의 수 N
N = int(input())

dynamic_programming(N)
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

(2) 규칙 찾기 => 규칙 틀림
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

(3) dp로 풀기 => X

(4) 백트래킹 => 조합 사용: 중복 없이 만들기
"""
# 각 문자의 수
rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50}
romes = ['I', 'V', 'X', 'L']
# 중복 수 제거를 위한 set
duplications = set()


# 백트래킹 함수
def back_tracking(used, total, start):
    # 문자가 다 쓰인 경우 set에 넣기
    if used == N:
        duplications.add(total)
        return

    # 4개의 문자 반복
    for i in range(start, 4):
        back_tracking(used + 1, total + rome[romes[i]], i)


# 사용할 수 있는 문자의 수 N
N = int(input())

# 사용된 숫자 수
used = 0
# 숫자의 합
total = 0
# 시작 문자
start = 0

back_tracking(used, total, start)
print(len(duplications))
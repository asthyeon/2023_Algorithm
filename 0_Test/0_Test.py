import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 야구공
1. 한 이닝에 3아웃이 발생하면 공수 교대
2. 야구랑 룰 같음
3. 1번 선수가 4번 타자 고정
* 입력
- 첫째 줄: 이닝 수 N
- 둘째 줄 ~ N개의 줄: 각 선수가 각 이닝에서 얻는 결과가 주어짐
 - 1: 안타, 2: 2루타, 3: 3루타, 4: 홈런, 0: 아웃
[출력: 얻을 수 있는 최대 점수 출력]
"""

"""
@ 풀이
(1) 그냥 풀어보기
"""


# 경기
def play(players):
    # 아웃 카운트
    out = 0




# 이닝 수 N
N = int(input())
# 각 이닝 정보
for _ in range(N):
    # 각 선수별 정보
    players = list(map(int, input().split()))


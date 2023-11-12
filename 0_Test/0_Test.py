import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 램프
[출력: K번 누른 후에 켜져있는 행의 최댓값 구하기]
1. 각 열의 아래에는 스위치가 달려 있음
2. 스위치를 누를 때마다 열에 있는 램프의 상태가 바뀜
3. 스위치를 K번 누르는데 중복 가능
4. 어떤 행에 있는 램프가 모두 켜져있을 때 행이 켜져있다고 말함
5. 스위치를 K번 눌러서 켜져있는 행을 최대로 하기
@ 풀이
(1) bfs로 1번씩 모든 열 점검하기
"""
from collections import deque
duplications = {}


# bfs 함수
def bfs():
    q = deque([])

    while q:




# 행 N, 열 M
N, M = map(int, input().split())
# 램프의 상태
lamp = [list(map(str, input().rstrip())) for _ in range(N)]
# 스위치 누르는 회수 K
K = int(input())
print(lamp)




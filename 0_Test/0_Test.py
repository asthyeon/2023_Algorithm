import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 구슬 무게가 파악 가능하면 Y, 아니면 N 출력
1. 추를 이용해 구슬의 무게를 파악하기
@ 풀이
(1) dp로 풀기
(2) 
무게 0 1    2  3   4     5   6   7   8   9   10   11   12   13   14   15
  추 
  2   0    2  0   0     
  3   3-2  2  3   0
  3   3-2  2   3   3+3-2
  3   3-2  2   3   3+3-2
 
"""

# 추의 개수
weights = int(input())
# 추의 무게들
weights_list = list(map(int, input().split()))
# 구슬의 개수
marbles = int(input())
# 구슬의 무게들
marbles_list = list(map(int, input().split()))












import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# C 개의 공유기를 N 개의 집에 적당히 설치 후 가장 인접한 두 공유기 사이의 거리를 최대로 구하기
1. 한 집에는 공유기 하나만 설치 가능
2. 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치
"""

# 집 수 N, 공유기 수 C
N, C = map(int, input().split())

# ㅈ
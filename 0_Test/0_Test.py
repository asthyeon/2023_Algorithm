import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 1번역에서 N번역으로 가는데 방문하는 최소 역의 수 구하기
1. 하이퍼튜브 하나는 역 K개를 서로 연결
2. 갈 수 없다면 -1 출력
@ 풀이
(1) 다익스트라 이용시 메모리 초과
(2) 연결정보를 다 받아놓고 1부터 N까지 순회
"""
import heapq


# 연결 함수
def connect(hyper):
    cnt = 0
    passed = [0] * (N + 1)
    passed[1] = 1
    for i in range(1, N):
        if passed[-1] != 0:
            break
        for j in range(M):
            if i in hyper[j]:
                for k in range(K):
                    if i == hyper[j][k]:
                        continue
                    if passed[hyper[j][k]] != 0:
                        continue
                    if passed[i] != 0:
                        passed[hyper[j][k]] = passed[i] + 1
    if passed[-1] == 0:
        return -1
    else:
        return passed[-1]


# 역의 수 N, 역의 개수 K, 하이퍼튜브의 개수 M
N, K, M = map(int, input().split())
hyper = []
for _ in range(M):
    tube = tuple(map(int, input().split()))
    hyper.append(tube)

print(connect(hyper))
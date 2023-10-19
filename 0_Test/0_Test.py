import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 김지민과 임한수가 몇 라운드에서 대결하는지 출력
1. 인접한 번호끼리 스타 진행
2. 이긴 사람은 다음 라운드 진출, 진 사람은 탈락
3. 참가자가 홀수라면 마지막 번호 참가자는 다음 라운드 자동 진출
4. 다음 라운드에선 다시 참가자의 번호를 1번부터 매긴다
5. 1명이 남을 때까지 라운드 계속 진행
6. 김지민과 임한수는 서로 만나기 전까지 항상 이김
7. 서로 대결하지 않으면 -1 출력
"""
sys.setrecursionlimit(10**9)


# 토너먼트 함수
def tournament(N, players, kim, lim, number):
    # 다음 라운드에 올라갈 인원
    match = []
    # 다음 라운드에 붙일 번호
    num = 0
    while True:
        if kim + lim == kim + kim + 1:

    # 참가자 수가 홀수라면 부전승 추가
    if N // 2 == 1:
        num += 1
        match.append(num)
    # 라운드 수 증가
    number += 1
    # 참가자 리스트 교체
    players = match[:]
    # 참가자 수 변경
    N = len(match)
    # 다음 라운드 진행
    tournament(N, players, kim, lim, number)


# 참가자 수 N, 김지민 번호, 임한수 번호
N, kim, lim = map(int, input().split())
# 참가자 리스트
players = [i for i in range(1, N + 1)]
# 라운드 수
number = 1

tournament(N, players, kim, lim, number)
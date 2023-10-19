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


# 토너먼트 함수
def tournament(p1, p2, number):
    while True:
        # 둘이 붙었을 때 종료
        if p1 + p2 == p1 + (p1 + 1) or p2 + p1 == p2 + (p2 + 1):
            # p1 이 짝수가 아니라면 라운드 수 출력
            if p1 % 2 != 0:
                print(number)
                return
            # p1 이 짝수라면 다음 라운드로 올리기
            else:
                p1 = (p1 + 1) // 2
                p2 = (p2 + 1) // 2
                number += 1
        # 둘이 붙지 않으면
        else:
            p1 = (p1 + 1) // 2
            p2 = (p2 + 1) // 2
            number += 1


# 참가자 수 N, 김지민 번호, 임한수 번호
N, kim, lim = map(int, input().split())
# 작은 번호를 p1, 큰 번호를 p2 로 지정
if kim < lim:
    p1 = kim
    p2 = lim
else:
    p1 = lim
    p2 = kim
# 라운드 수
number = 1

tournament(p1, p2, number)
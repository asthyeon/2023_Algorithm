import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# Yonsei TOTO
[출력: 주어진 마일리지로 최대로 들을 수 있는 과목 개수 출력]
1. 듣고 싶은 과목에 마일리지 1~36 분배 가능
2. 마일리지를 많이 투자한 순으로 그 과목의 수강인원만큼 신청됨
3. 마일리지가 같으면 성준이에게 우선순위가 주어짐
@ 풀이
(1) 각 과목별로 최소로 들일 수 있는 마일리지 계산하기
(2) 주어진 마일리지로 최소값부터 분배
"""

# 과목수 n, 주어진 마일리지 m
n, m = map(int, input().split())
# 각과목별 필요한 마일리지
needs = []
# 과목마다 주어지는 정보
for _ in range(n):
    # 과목 신청한 사람 수 P, 수강인원 L
    P, L = map(int, input().split())
    # 각 사람이 마일리지를 얼마나 넣었는지 주어짐
    mileages = list(map(int, input().split()))
    
    # 마일리지 역순 정렬
    mileages.sort(reverse=True)
    
    # 성준이가 넣어야할 마일리지
    # 신청한 사람이 수강인원보다 많거나 같다면
    if P >= L:
        need = mileages[L - 1]
        needs.append(need)
    # 수강인원이 더적다면 마일리지는 최소값 1
    else:
        need = 1
        needs.append(need)
# 필요한 마일리지 정렬
needs.sort()
# 들을 수 있는 과목 수
cnt = 0
# 과목수 계산
for need in needs:
    if need > 36:
        break
    if m >= need:
        cnt += 1
        m -= need
    else:
        break

print(cnt)


import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# A시, B분, C초
A, B, C  = map(int, input().split())
# 요리하는데 필요한 시간 D초
D = int(input())

# C초 에 D 나머지를 더하기
C += D % 60
# D초 는 D분 으로 변환
D = D // 60
# 만약 60초를 넘긴다면
if C >= 60:
    # C초 - 60초
    C -= 60
    # B분 + 1분
    B += 1

# B분 에 D 분 나머지 더하기
B += D % 60
# D분 은 D시 로 변환
D = D // 60
# 만약 60분을 넘긴다면
if B >= 60:
    # B분 - 60분
    B -= 60
    # A시 + 1시
    A += 1

# A시 에 D 시 나머지 더하기
A += D % 24
# 만약 A시가 24시를 넘어간다면
if A >= 24:
    # 0시로 바꿔주기
    A -= 24

print(A, B, C)


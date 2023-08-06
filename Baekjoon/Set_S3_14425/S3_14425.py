import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# set 를 이용하기
'''

# 집합 S 에 포함된 문자열의 수: N, 검사해야하는 문자열 수: M
N, M = map(int, input().split())

# 집합 S 형성
S = set()
for i in range(N):
    name = input().strip()
    S.add(name)

# 검사할 카운트 생성
count = 0

# 검사하기
for i in range(M):
    check = input().strip()
    if check in S:
        count += 1

print(count)
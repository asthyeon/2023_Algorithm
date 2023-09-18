import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# N 개의 수가 주어졌을 때 네가지 기본 통계값 구하기
1. 산술평균: 합을 N으로 나눈 값, 소수점 이하 첫째 자리에서 반올림한 값
2. 중앙값: 중앙에 위치하는 값
3. 최빈값: 가장 많이 나타나는 값, 여러개 있을 때는 두번째로 작은 값 출력
4. 범위: 최댓값 - 최솟값
"""

# 수의 개수 N
N = int(input())

# N개의 정수들
N_list = []
for _ in range(N):
    N_list.append(int(input()))
# 정렬
N_list.sort()

# 산술평균
print(int(round((sum(N_list) / N), 0)))

# 중앙값
print(N_list[N // 2])

# 최빈값
N_dict = {}
for n in N_list:
    if n not in N_dict:
        N_dict[n] = 1
    else:
        N_dict[n] += 1
# 정렬
sorted(N_dict, reverse=True)
# 최빈값 찾기
cnt = 0
many = 0
m_list = []
for d in N_dict:
    if cnt < N_dict[d]:
        cnt = N_dict[d]
        many = d
# 중복 확인
duple = 0
for d in N_dict:
    if N_dict[d] == cnt:
        duple += 1
        m_list.append(d)
# 정렬
m_list.sort()
# 최빈값 출력
if duple >= 2:
    print(m_list[1])
else:
    print(many)

# 범위
print(N_list[-1] - N_list[0])







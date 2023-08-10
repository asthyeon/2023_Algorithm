import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 포켓몬 도감 만들기
# 리스트로 출력하면 시간초과이므로 딕셔너리 사용
1. 빈 딕셔너리를 만들고
2. 포켓몬을 다 집어넣기
3. 번호로 부를 딕셔너리 1개 만들기
4. 이름으로 부를 딕셔너리 1개 만들기
'''

# 도감 수록 포켓몬 수 N, 맞춰야 하는 문제 수 M
N, M = map(int, input().split())

# 포켓몬 도감 딕셔너리
poketmon_name = {}
poketmon_num = {}

# N 개의 줄에 포켓몬 하나씩 입력
for i in range(1, N + 1):
    name = input()
    poketmon_name[name.strip()] = i
    poketmon_num[i] = name.strip()

# 출력하기
for i in range(M):
    ans = input().strip()
    if ans.isdigit():
        print(poketmon_num[int(ans)])
    else:
        print(poketmon_name[ans])
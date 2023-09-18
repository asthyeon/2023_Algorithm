import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 최대 사용할 수 있는 회의의 최대 개수 출력
1. 각 회의 I 에 대해 시작시간과 끝나는 시간이 주어져있음
2. 각 회의가 겹치지 않게 하면서 회의실 사용할 수 있는 최대 개수 찾아보기
"""

# 회의의 수
N = int(input())
# 회의 리스트
N_list = []
# 시작시간과 끝나는 시간
for _ in range(N):
    s, e = map(int, input().split())
    N_list.append((s, e))

# 끝나는 시간 순 - 시작 시간 순 정렬
N_list = sorted(N_list, key=lambda x: (x[1], x[0]))
# 회의 수
cnt = 0
end = 0
for i in range(N):
    if end <= N_list[i][0]:
        cnt += 1
        end = N_list[i][1]

print(cnt)

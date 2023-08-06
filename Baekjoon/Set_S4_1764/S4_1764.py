import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 딕셔너리 이용하기
1. 듣도 못한 사람 구하기
2. 보도 못한 사람 구하기
3. 겹치는 사람을 리스트에 넣기
4. 리스트 정렬 후 출력
'''

# 듣도 못한 사람 수 N, 보도 못한 사람 수 M
N, M = map(int, input().split())

# 듣도 못한 사람 수 명단
listen = {}
for i in range(N):
    name = input()
    listen[name.strip()] = name.strip()

# 보도 못한 사람 수 명단
see = {}
for i in range(M):
    name = input()
    see[name.strip()] = name.strip()

# 듣보잡 구하기
unknown = []
for i in listen:
    if i in see:
        unknown.append(i)

# 듣보잡 사전순 정렬
unknown.sort()

# 출력
print(len(unknown))
for i in unknown:
    print(i)
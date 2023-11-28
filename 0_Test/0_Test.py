import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 접두사 찾기
[출력: M 개의 문자열 중에 총 몇 개가 포함되어 있는 문자열 중 적어도 하나의 접두사인지 출력]
1. 접두사: 가장 앞에서부터 부분 문자열
2. 집합 S에 포함되어 있는 문자열 중 적어도 하나의 접두사인 것의 개수를 구하기
@ 풀이
(1) 그냥 풀어보기 => 시간초과
(2) 맞는 단어를 체크할 때 이분탐색 사용
"""


N, M = map(int, input().split())
tri = dict()
for _ in range(N):
    string = list(input().strip())
    target = tri
    for i in range(len(string)):
        if string[i] not in target:
            target[string[i]] = dict()
        target = target[string[i]]
    print(tri)

result = 0
for _ in range(M):
    string = list(input().strip())
    target = tri
    for i in range(len(string)):
        if string[i] not in target:
            print(string, i)
            break
        target = target[string[i]]
    else:
        result += 1

print(result)
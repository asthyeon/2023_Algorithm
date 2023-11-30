import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 디스크 트리
[출력: 디렉토리 구조를 보기 좋게 출력, 공백은 깊이, 사전순으로 출력]
1. 디렉토리의 전체 경로가 모두 주어졌을 때 디렉토리 구조를 구해 보기 좋게 출력하기
2. 경로는 한 줄로 이루어짐, 공백 포함 X
@ 풀이
(1) 트라이 사용
"""


# 경로 탐색 함수
def search(directories, level):
    # 정렬된 디렉토리의 key와 value를 이용
    for key, value in sorted(directories.items()):
        # 공백을 포함하여 level 에 따라 key 출력
        print(' ' * level + key)
        # 다음 value로 재귀
        search(value, level + 1)


# 디렉토리 전체 경로의 개수 N
N = int(input())
# 디렉토리 저장
directories = {}
for _ in range(N):
    # 경로 입력
    routes = input().strip().split('\\')
    # 현재위치
    current = directories
    # 경로 저장
    for route in routes:
        # 현재위치에 경로가 없다면 저장
        if route not in current:
            current[route] = {}
        # 현재위치 이동
        current = current[route]

search(directories, 0)
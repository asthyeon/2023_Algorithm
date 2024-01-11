import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 텀 프로젝트
1. 프로젝트 팀을 만들기 위해 모든 학생등를 함께하고 싶은 학생들을 선택해야 함
 - 프로젝트 팀원 수에는 제한 X(모든 학생들이 동일한 팀의 팀원인 경우 한 팀만 만들어짐)
 - 한 명당 한 명만 선택 가능
 - 혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능
2. 주어진 선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하기
* 입력
- 첫째 줄 T: 테스트 케이스의 개수
- 각 테스트의 첫째 줄 n: 학생의 수
- 각 테스트의 둘째 줄: 선택된 학생들의 번호가 주어짐
[출력: 각 줄에 프로젝트 팀에 속하지 못한 학생들의 수 나타내기]
"""

"""
@ 풀이
(1) 예시 이해해보기
1 -> 3 X
2 -> 1 X
3 -> 3 (3)팀
4 -> 7 (4, 6, 7)팀
5 -> 3 X
6 -> 4 (4, 6, 7)팀
7 -> 6 (4, 6, 7)팀
(2) dfs로 탐색
(3) 시간초과 지옥 -> 재귀로 풀기
"""
sys.setrecursionlimit(10**9)


# dfs 함수
def dfs(start, project):
    # 숫자 사용
    used[start] = 1
    # 이번 팀 멤버 추가
    team.append(start)
    # 이동
    start = choices[start]

    # 사용한 번호인지 체크
    if used[start] == 1:
        # 싸이클이라면 싸이클 시작 지점부터 프로젝트 참여자에 추가
        if start in team:
            project += team[team.index(start):]
    # 사용한 번호가 아니라면 재귀
    else:
        dfs(start, project)


# 테스트 케이스 수
T = int(input())
for tc in range(1, T + 1):
    # 학생 수 n
    n = int(input())
    # 학생들이 선택한 번호(편의를 위해 0번 추가)
    choices = [0]
    choices += list(map(int, input().split()))
    # cnt, use = 0, 0
    # 팀 프로젝트 참여자들
    project = []
    # 사용된 숫자 리스트
    used = [0] * (n + 1)
    # dfs 탐색
    for start in range(1, n + 1):
        if used[start] == 0:
            # 이번 팀
            team = []
            dfs(start, project)
            # use += 1
            # print(f'호출: {use}')
    # print(project)
    print(n - len(project))










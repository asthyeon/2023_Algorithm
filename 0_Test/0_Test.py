import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 걸그룹 마스터 준석이
[출력: 퀴즈의 종류가 0 = 멤버이름 사전순 출력, 1 = 해당 멤버가 속한 팀의 이름 출력]
1. 걸그룹 개인과 팀의 이름을 검색하여 외우게 하는 프로그램 만들기
"""
# 팀 딕셔너리
teams = {}
# 팀 이름 배열
team_names = []

# 걸그룹 수 N, 맞혀야 할 문제 M
N, M = map(int, input().split())
# 걸그룹 정보
for _ in range(N):
    # 팀이름
    team = input().rstrip()
    team_names.append(team)
    # 멤버 수
    cnt = int(input())
    teams[team] = []
    # 멤버 정보 넣기
    for _ in range(cnt):
        # 멤버
        member = input().rstrip()
        teams[team].append(member)
    # 멤버 사전순으로 정렬
    teams[team].sort()

# M 개의 퀴즈
for _ in range(M):
    # 팀의 이름이나 멤버 이름
    name = input().rstrip()
    # 퀴즈타입
    quiz = int(input())

    # 팀의 이름이 주어질 때
    if quiz == 0:
        for mem in teams[name]:
            print(mem)
    # 멤버의 이름이 주어질 때
    else:
        for team_name in team_names:
            if name in teams[team_name]:
                print(team_name)

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 현재 회사에 있는 사람의 이름을 기록하기
# 리스트로 출력하면 시간초과이므로 딕셔너리 사용
1. 빈 딕셔너리를 만들고
2. 현재 상태를 체크한 후
3. 출근 상태면 빈 딕셔너리에 이름 넣기
4. 퇴근 상태거나 퇴근 할 경우 빈 리스트에서 이름 제거
5. 딕셔너리를 역순으로 정렬 후 출력
'''

# 로그에 기록된 출입 기록의 수
n = int(input())

# 현재 회사에 있는 사람의 리스트
company = {}

# n 개의 줄에 출입 기록
for i in range(n):
    # 각 사람의 이름과 출퇴근 여부 입력
    name, commute = input().split()
    if commute == 'enter':
        company[name] = name
    else:
        if name in company:
            company.pop(name)

# 역순으로 정렬
sort_company = sorted(company, reverse=True)

# 한줄씩 출력
for i in sort_company:
    print(i)


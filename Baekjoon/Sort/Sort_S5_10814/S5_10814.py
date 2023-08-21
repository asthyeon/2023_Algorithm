import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 나이순 정렬
* 나이가 같으면 먼저 가입한 사람이 앞에 옴
'''

# 회원 수 N
N = int(input())

# 정렬
members = {}
# 나이순 정렬
ages = []
for i in range(N):
    age, name = input().split()
    ages.append(int(age))
    # 기존 멤버가 있다면
    if int(age) in members:
        members[int(age)].append(name)
    # 기존 멤버가 없다면
    else:
        members[int(age)] = [name]

# 나이 정렬
ages.sort()
# 중복이 없는 값만 넣기
results = []
for age in ages:
    if age not in results:
        results.append(age)

# 나이와 이름 출력
for result in results:
    for i in range(len(members[result])):
        print(result, members[result][i])

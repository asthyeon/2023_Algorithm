import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 전공평점 계산기 만들기
1. 등급이 p인 과목은 계산에서 제외
2. 20줄이 주어짐
"""

# 각 등급별 점수
score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0,
         'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
# 과목 수
cnt = 0
# 총 점수
total = 0
# 총 이수학점
total_credit = 0
# 입력받기
for _ in range(20):
    subject, credit, grade = map(str, input().split())

    # 과목 평점이 P가 아닐 때
    if grade != 'P':
       total_credit += float(credit)
       total += float(credit) * score[grade]

print(total / total_credit)

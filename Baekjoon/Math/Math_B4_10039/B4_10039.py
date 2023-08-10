import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

# 학생 5명의 점수가 주어졌을 때 평균 점수를 구하기
averages = []
for i in range(5):
    grade = int(input())
    # 40점 미만일 때는 40점으로 평가
    if grade < 40:
        grade = 40
    averages.append(grade)

# 평균 구하기
print(int(sum(averages) / 5))
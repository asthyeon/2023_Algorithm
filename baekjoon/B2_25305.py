import sys
sys.stdin = open("input.txt", "r")

# 응시자의 수: N, 상을 받는 사람의 수: k
N, k = map(int, input().split())

# 점수 받고 리스트로 만들기
grade = list(map(int, input().split()))

# 내림차순 정렬
grade.sort(reverse=True)

# k번째까지 출력이므로 인덱스 번호: k-1
print(grade[k - 1])
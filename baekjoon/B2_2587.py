import sys
sys.stdin = open("input.txt", "r")

# 정렬을 사용할 빈 리스트 만들기
sorting = []
# 평균을 구할 숫자 만들기
numb = 0
# 총 입력받을 수 5개의 자연수 받기
for i in range(5):
    N = int(input())
    # 리스트에 자연수 넣기
    sorting.append(N)
    # numb에 숫자 더하기
    numb += N

# 평균 출력
print(int(numb/5))
# 중앙값 정렬
sorting.sort()
# 중앙값 출력
print(sorting[2])




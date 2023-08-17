import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 칸토어 집합
1. 0과 1 사이의 실수로 이루어진 집합
2. 구간 [0, 1] 에서 시작해서 각 구간을 3등분 하여 가운데 구간을 반복적으로 제외하는 방식
3. 전체 집합이 유한이라고 가정하고 다음과 같은 가정을 통해 칸토어 집합의 근사 만들기
    (1) -가 3^N개 있는 문자열에서 시작
    (2) 문자열을 3등분한 뒤, 가운데 문자열을 공백으로 바꾸기, 선(문자열) 2개 남음
    (3) 이제 각 선(문자열)을 3등분하고, 가운데 문자열을 공백으로 바꾸기
    (4) 이 과정은 모든 선의 길이가 1일때 까지 계속하기
'''


# 분할 정복 함수
def divide(N, S, E, arr):
    if N == 0:
        return

    M = (E - S) // 3
    # 왼쪽
    divide(N - 1, S, S + M, arr)
    # 중간 공백 형성
    for i in range(S + M, S + (M * 2)):
        arr[i] = ' '
    # 오른쪽
    divide(N - 1, S + (M * 2), S + (M * 3), arr)


while True:
    try:
        N = int(input())
        # 시작점과 끝점
        S = 0
        E = (3 ** N)
        # 배열 형성
        arr = ['-'] * (3 ** N)

        divide(N, S, E, arr)
        result = "".join(arr)
        print(result)
    except:
        break



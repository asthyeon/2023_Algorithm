import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

'''
# 하노이 탑 이동
1. 한 번에 한개의 원판만 이동
2. 쌓아 놓은 원판은 항상 위의 것이 아래 것보다 작아야 함
3. 3 개의 장대 존재
'''

# 이동 횟수 재귀 함수
def moving(N):
    if N == 1:
        return 1
    else:
        K = moving(N - 1) + (2 ** (N - 1))
        return K


# 재귀 함수 생성
def hanoi(N, start, middle, end):
    # 자기 자신만 남을 때 그대로 이동하고 재귀 종료
    if N == 1:
        # 이동한 위치 출력
        print(start, end)
        return

    # 원반을 출발지에서 도착지를 통해서 경유지로 옮기는 경우
    hanoi(N - 1, start, end, middle)
    # 이동한 위치 출력
    print(start, end)
    # 원반을 경유지에서 출발지를 통해서 도착지로 옮기는 경우
    hanoi(N - 1, middle, start, end)


# 원판의 개수 N
N = int(input())
# 이동 횟수
print(moving(N))
# 출발지, 경유지, 도착지
A, B, C = 1, 2, 3
hanoi(N, A, B, C)


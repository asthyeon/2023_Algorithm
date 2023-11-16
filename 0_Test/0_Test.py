import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 전구와 스위치
[출력: 답 출력, 불가능시 -1 출력]
1. 스위치를 누르면 상태가 반대로 됨(i번 스위치 -> i-1, i, i+1 상태 체인지)
2. 1번 스위치: 1, 2번 체인지
   N번 스위치: N-1, N번 체인지
3. 우리가 만들고자 하는 상태가 주어질 때 최소 몇 번 누르면 되는가
@ 풀이
(1) 덱을 사용해 하나씩 체크하면서 바꾸기
(2) 딕셔너리를 이용해 중복 체크하기
=> 메모리 초과

(1) 3개씩만 동일하므로 그 부분이 목표와 동일하다면 넘어가는 방식으로 진행하기
 - 2번 스위치부터 시작해서 이전 번호가 다르다면 누르는 방식으로 진행하기
 - 1번 스위치를 누른 경우와 2번 스위치를 누른 경우 비교 
(2) 메모리 초과를 방지하기 위해 덱 사용 X
(3) 1번 스위치 온오프를 미리 바꿔서 함수를 2번 써보기
"""


# 체크 함수
def switch(now, target):
    # 스위치 누른 횟수
    cnt = 0
    # 스위치 누르기
    pushed = now[:]
    for i in range(1, N):
        # 이전 전구 상태가 목표 전구 상태와 다르다면 누르기
        if pushed[i - 1] != target[i - 1]:
            # 스위치 횟수 추가
            cnt += 1
            if pushed[i - 1] == 1:
                pushed[i - 1] = 0
            else:
                pushed[i - 1] = 1
            if pushed[i] == 1:
                pushed[i] = 0
            else:
                pushed[i] = 1
            # N번 스위치가 아닐 때는 다음 번호까지 바꾸기
            if i != N - 1:
                if pushed[i + 1] == 1:
                    pushed[i + 1] = 0
                else:
                    pushed[i + 1] = 1

        # 목표와 일치하면 종료
        if pushed == target:
            return cnt

    # 불가능시
    return -1


# 전구 수 N
N = int(input())
# 전구의 현재 상태
now = list(map(int, input().rstrip()))
# 만들고자 하는 전구의 상태
target = list(map(int, input().rstrip()))

# 현재 상태가 목표라면 바로 종료
if now == target:
    print(0)
# 현재 상태가 목표가 아니라면
else:
    # 1번 스위치를 안눌렀을 때
    off = switch(now, target)
    # 불가능하지 않으면 출력
    if off != -1:
        print(off)
    # 1번 스위치 누르기
    else:
        if now[0] == 0:
            now[0] = 1
        else:
            now[0] = 0
        if now[1] == 0:
            now[1] = 1
        else:
            now[1] = 0
        on = switch(now, target)
        # 불가능 여부 체크 후 출력
        if on != -1:
            print(on + 1)
        else:
            print(on)







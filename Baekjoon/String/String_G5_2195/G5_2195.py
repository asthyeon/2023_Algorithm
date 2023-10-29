import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# copy 함수의 최소 사용횟수
1. 원본 문자열 S가 주어졌을 때 부분을 복사하여 P라는 새로운 문자열을 만들려고 함
2. 복사를 할 때에는 copy(s, p) 함수 이용
    - S의 s번 문자부터 p개의 문자를 P에 복사해서 붙인다
@ 풀이
(1) 만들 문자열의 뒤에서부터 하나씩 줄여가면서 원본 문자열과 비교하며 찾기
(2) 일치하는 부분이 있다면 일치하는 부분부터 다시 마지막위치으로 돌아가서 1번 반복
"""


# copy 함수
def copy(S, P):
    # copy 횟수
    cnt = 0
    # 문자열 인덱스 값
    idx = 0
    # 비교할 인덱스 값
    last_idx = len(P)
    while True:
        # 인덱스 값이 문자열의 길이와 같아진다면 종료
        if idx == len(P):
            break
        # 문자열이 S에 있다면
        if P[idx:last_idx] in S:
            # 문자열 길이만큼 추가
            idx += last_idx - idx
            # 마지막 인덱스 초기화
            last_idx = len(P)
            # 함수 사용횟수 추가
            cnt += 1
        # 문자열이 S에 없다면 마지막 인덱스 -1
        else:
            last_idx -= 1

    return cnt


# 원본 문자열 S
S = input().strip()
# 새로운 문자열 P
P = input().strip()

print(copy(S, P))
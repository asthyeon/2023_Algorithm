import sys
sys.stdin = open('input.txt')

'''
# 어떤 문자열이 팰린드롬인지 판별하기
'''

T = int(input())
for tc in range(1, T + 1):
    S = input()

    # 함수 호출 횟수
    cnt = 0

    # 재귀함수
    def recursion(S, l, r):
        # 함수 호출 횟수를 세기 위한 변수
        global cnt
        cnt += 1
        # 모든 글자를 확인했을 경우
        if l >= r:
            return 1
        # 맨처음 글자와 맨 끝 글자가 다를 경우
        elif S[l] != S[r]:
            return 0
        # 비교할 글자가 같다면 다음 글자 비교를 위해 재귀 호출
        else:
            return recursion(S, l+1, r-1)

    # 팰린드롬 확인 함수
    def isPalindrome(S):
        return recursion(S, 0, len(S)-1)

    print(isPalindrome(S), cnt)
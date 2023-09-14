import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 특정 문자열 구간에서 특정 문자가 몇 번 나타나는지 구하기
1. 알파벳이 중지나 검지 위치에 오는 알파벳인지 확인하면 실용적인지 확인 가능
2. 문자열의 문자는 0번째부터 세며, l번째와 r번째 문자를 포함해서 생각
3. 같은 문자열을 두고 q번 질문함
@ 풀이
(1) 시간초과를 해결하기 위해 누적 합을 미리 만들어 놓아야 함
"""

# 문자열: S
S = ' ' + input().rstrip()

# 구간 합 만들기
pre_sum = dict()
for i in range(1, len(S)):
    if S[i] in pre_sum:
        continue
    else:
        pre = [0] * len(S)
        for j in range(1, len(S)):
            # 같은 문자라면 이전 값 + 1
            if S[i] == S[j]:
                pre[j] = pre[j - 1] + 1
            # 다른 문자라면 현재 값 = 이전 값
            else:
                pre[j] = pre[j - 1]
        # 딕셔너리에 넣기
        pre_sum[S[i]] = pre

# 질문의 수
q = int(input())

# 질문 받기
for _ in range(q):
    # 문자 alp, l 부터 r 까지
    alp, l, r = map(str, input().split())

    # 딕셔너리에 없는 문자가 나올 경우
    if alp not in pre_sum:
        print(0)

    # r 번째 값에서 l - 1 번째 값을 빼주면 결과값
    else:
        result = pre_sum[alp][int(r) + 1] - pre_sum[alp][int(l)]
        print(result)
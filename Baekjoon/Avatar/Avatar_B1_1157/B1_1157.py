import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 주어진 단어에서 가장 많이 사용된 알파벳을 대문자로 출력
1. 알파벳이 여러 개 존재하는 경우 '?' 출력
"""

# 주어진 단어
word = input().rstrip()

# 각 단어 주어진 횟수 구하기
cnt_dict = {}
for alp in word:
    if alp.upper() not in cnt_dict:
        cnt_dict[alp.upper()] = 1
    else:
        cnt_dict[alp.upper()] += 1

# 리스트로 만들기
cnt_list = []
for key, val in cnt_dict.items():
    cnt_list.append((key, val))

# 나온 횟수로 정렬
cnt_list = sorted(cnt_list, key=lambda x: x[1], reverse=True)

# 가장 많은 단어 수가 여러 개인지 확인
if len(cnt_list) > 1:
    if cnt_list[0][1] == cnt_list[1][1]:
        print('?')
    else:
        print(cnt_list[0][0])
else:
    print(cnt_list[0][0])

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 크로아티아 알파벳이 몇 개 사용되었는지 확인
1. 변경 목록에 없는 알파벳은 1글자로 처리
2. 위 목록에 없는 알파벳은 1글자
3. '-', '=' 은 글자 X
"""

# 크로아티아 알파벳(변경 목록)
croatia = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')
# 첫글자만 딴 경우
first = ('c', 'd', 'l', 'n', 's', 'z')
# 특수문자
special = ('-', '=')

# 주어진 단어
word = input().rstrip()

# 알파벳 확인
cnt = 0
check = ''
for alp in word:
    # check 에 알파벳이 들어있으면
    if len(check) >= 1:
        check += alp
        # dz일 경우 다음으로 넘김
        if check == 'dz':
            continue
        # 크로아티아 알파벳이라면 cnt +1
        elif check in croatia:
            cnt += 1
            check = ''
        # 크로아티아 알파벳이 아니라면 단어 길이 및 현재 글자에 따라 조건 형성
        else:
            # 단어 길이가 3일 때
            if len(check) == 3:
                # 현재 글자가 특수문자라면 cnt +2
                if alp in special:
                    cnt += 2
                    check = ''
                # 현재 글자가 특수문자가 아니라면
                else:
                    # 현재 글자가 변경문자 첫글자라면 cnt +2 및 check 에 넣기
                    if alp in first:
                        cnt += 2
                        check = alp
                    # 현재 글자가 그냥 알파벳이라면 cnt +3
                    else:
                        cnt += 3
                        check = ''
            # 단어 길이가 2일 때
            else:
                # 현재문자가 특수문자라면 cnt +1
                if alp in special:
                    cnt += 1
                    check = ''
                # 현재 문자가 특수문자가 아니라면
                else:
                    # 변경 문자의 첫글자라면 cnt +1 및 check에 넣기
                    if alp in first:
                        cnt += 1
                        check = alp
                    # 현재 문자가 알파벳이라면 cnt +2
                    else:
                        cnt += 2
                        check = ''
    # check가 비어있다면
    else:
        # 변경문자의 첫글자에 해당한다면
        if alp in first:
            check = alp
        # 특수문자가 아니라면 cnt +1
        else:
            if alp not in special:
                cnt += 1
# 반복문을 다 돌고 check가 비어있지 않을 경우
else:
    if len(check) == 1:
        if check[-1] not in special:
            cnt += 1
    elif len(check) == 2:
        if check[-1] not in special:
            cnt += 2

print(cnt)
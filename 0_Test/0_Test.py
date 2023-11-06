import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 정규표현식 사용
1. 정규표현식(정규식)
 - 복잡한 문자열을 처리할 때 사용하는 기법
 - re 모듈: 정규 표현식 지원
 - compile: 정규 표현식을 컴파일
 - match(): 문자열의 처음부터 정규식과 매치되는지 조사
 - fullmatch(): 문자열의 남는 부분 없이 완벽하게 일치하는지 검사
 - search(): 문자열 전체를 검색하여 정규식과 매치되는지 조사
 - findall(): 정규식과 매치되는 모든 문자열을 리스트로 리턴
 - finditer(): 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 리턴
"""

import re

# 정규 표현식을 컴파일
p = re.compile('(100+1+|01)+')

T = int(input())
for tc in range(1, T + 1):
    # 전파 입력
    spread = input().strip()
    # 정규식과 매치된다면 예스
    if p.fullmatch(spread):
        print('YES')
    # 매치되지 않으면 노
    else:
        print('NO')







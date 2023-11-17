import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

"""
# 기적의 매매법
[출력: 준현이 자산이 더 크면 "BNP", 반대는 "TIMING", 같다면 "SAMESAME"]
1. 준현이: 절대 팔지 않음 
 - 주식을 살 수 있다면 가능한 만큼 즉시 매수
2. 성민이: 33매매법
 - 모든 거래는 전량 매수 전량 매도
 - 3일 연속 상승주는 다음날 무조건 하락: 3일째 상승 = 전량 매도(반대도 성립)
3. 내기기간 1일 ~ 14일
4. 준현이와 성민이 중 누가 더 높은 수익률?
@ 풀이
(1) 구현하기
"""

# 준현이와 성민이에게 주어질 현금
cash = int(input())
# 각 일자의 주가
stocks = list(map(int, input().split()))

# 준현이 주식수, 현금
bnp_shares = 0
bnp_cash = cash
# 성민이 주식수, 현금
three_shares = 0
three_cash = cash

# 주식투자
for i in range(14):

    # 준현이는 항상 전량 매수
    bnp_shares += bnp_cash // stocks[i]
    bnp_cash = bnp_cash % stocks[i]
    
    # 성민이는 33매매법
    # 상승 3일째라면 전량 매도
    if stocks[i - 2] < stocks[i - 1] < stocks[i]:
        three_cash += three_shares * stocks[i]
        three_shares = 0
    # 하락 3일째~라면 전량 매수
    elif stocks[i - 2] > stocks[i - 1] > stocks[i]:
        three_shares += three_cash // stocks[i]
        three_cash = three_cash % stocks[i]

    print(f'#{i + 1}')
    print(f'shares: {three_shares}')
    print(f'cash: {three_cash}')

# 14일 후 자산 비교(남은 현금 + 주식 자산)
bnp = bnp_cash + (bnp_shares * stocks[-1])
three = three_cash + (three_shares * stocks[-1])
print(bnp, three)
if bnp > three:
    print('BNP')
elif bnp < three:
    print('TIMING')
else:
    print('SAMESAME')





### https://school.programmers.co.kr/learn/courses/30/lessons/42883

"""
 전체를 다 따져볼까? 재귀로 풀어볼까? 라는 생각을 했지만

 문제 제한을 보면
 number 길이 ≤ 1,000,000
 k ≤ number 길이

 그러면 재귀로하면 깊이가 백만까지 가는데
 파이썬 재귀 제한은 1000 임

 자 그렇다면 재귀로 모든경우를 다 보면 절대 못푼다는것을 알아야함
 "그리디" 라는 전략을 떠올려야함!!

 모든 케이스를 다 따지지말고 ...
 어차피 큰 수를 구하는거니까
 앞자리수가 큰게 오도록 해주면 되는거잖슴?

"""

def solution(number, k):
    stack = []

    for digit in number:

        # 스택에 숫자가 있고
        # 아직 지울 수 있는 횟수(k)가 남아 있고
        # 스택의 마지막 숫자보다 지금 숫자가 더 크다면
        #  앞에 있는 작은 숫자는 버리는 게 이득
        while len(stack) > 0 and k > 0 and stack[-1] < digit:
            stack.pop()   # 스택 맨 뒤 숫자 제거
            k -= 1        # 제거 횟수 1 감소

        # 지금 숫자는 스택에 넣는다
        stack.append(digit)

    # for문이 끝났는데도 k가 남아있는 경우
    # 앞에서 제거할 일이 없었으므로
    # 뒤에서부터 제거해야 가장 큰 수가 된다
    if k > 0:
        stack = stack[:-k]  # 뒤에서 k개 제거

    answer = ""
    for s in stack:
        answer += s

    return answer
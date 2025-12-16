### https://school.programmers.co.kr/learn/courses/30/lessons/12945


def solution(n):
    return fibo(n) % 1234567

def fibo(n) :
    if n == 0 :
        return 0
    if n == 1 or n == 2 :
        return 1
    return fibo(n-1) + fibo(n-2)

"""
이렇게 냅다 재귀로 풀면 -> 런타임에러 시간초과가 뜬다

재귀로 문제를 풀때면 n을 살펴보자!
>>> n은 2 이상 100,000 이하인 자연수입니다. 라고 써있잖아여?
파이썬은 재귀 depth가 1000까지밖에 안되기때문에... 이것은 재귀로 풀 수 없음..

자 그렇다면 어떻게 하면될까?
피보나치수열은 대표적인 동적계획법 문제이다! 
"""

def solution(n):
    MOD = 1234567

    dp = [0] * (n + 1) ## 값을 저장해놓을 배열을 만들어줌
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
        ## (a + b) % M == ((a % M) + (b % M)) % M

    return dp[n]

"""
그런데 여기서,,, 조금 더 개선할 수 있는 포인트가 있다
바로바로,,,! dp라는 배열 전체가 필요하지않다는것! 

현재 값을 알기위해서는 이전 두 값만 있으면 된다,,! 
n+1 길이의 배열이 아닌 변수 두개만 있으면 되는부분! 
"""

def solution(n):
    MOD = 1234567

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1  # fibo(0), fibo(1)

    for _ in range(2, n + 1):
        a, b = b, (a + b) % MOD

    return b




"""
왜 재귀 + 메모이제이션도 안 쓰는가?

이렇게 하면 되긴 함:

def solution(n):
    MOD = 1234567
    memo = {0: 0, 1: 1}

    def fibo(x):
        if x in memo:
            return memo[x]
        memo[x] = (fibo(x - 1) + fibo(x - 2)) % MOD
        return memo[x]

    return fibo(n)


하지만:

재귀 깊이 문제 여전히 존재

반복문이 더 안전하고 깔끔
"""

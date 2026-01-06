
### https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    # n을 k진수 문자열로 만들기
    s = ""
    while n > 0:
        s = str(n % k) + s
        n //= k

    # 소수 체크: i*i가 x를 넘기 전까지만 나눠보면 됨
    # 왜냐면 어떤 수 x가 합성수라면, x = a * b (a,b>1)인 두 약수가 반드시 존재하는데,
    # 적어도 하나는 sqrt(x) 이하이기 때문
    # 예: 36 = 4 * 9 (4 <= 6), 49 = 7 * 7 (7 <= 7)
    def is_prime(x):
        if x < 2:
            return False
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True

    # 0으로 끊어서 나온 조각들 중, 소수인 것만 카운트
    ans = 0
    for part in s.split('0'):
        if part == "":      # 연속된 0 때문에 빈 조각이 나올 수 있음
            continue
        if is_prime(int(part)):
            ans += 1

    return ans

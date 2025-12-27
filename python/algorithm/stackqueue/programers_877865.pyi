#  https://school.programmers.co.kr/learn/courses/30/lessons/77885
def solution(numbers):
    answer = []
    for x in numbers:
        if x % 2 == 0:
            # 짝수: 마지막 비트(0)만 1로 바뀌므로 1비트 차이
            answer.append(x + 1)
        else:
            # 홀수: y = x + 1 + ((x ^ (x+1)) >> 2)
            answer.append(x + 1 + ((x ^ (x + 1)) >> 2))
    return answer

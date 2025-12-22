## https://school.programmers.co.kr/learn/courses/30/lessons/131127

def solution(want, number, discount):
    answer = 0
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    # 할인 목록에서 10일짜리 구간을 하나씩 확인
    # len(discount) - 9 까지인 이유:
    # 10일을 보려면 시작 인덱스가 여기까지만 가능
    for start in range(len(discount) - 9):
        discount_dict = {}

        # 현재 시작점부터 10일 동안의 할인 상품 세기
        for i in range(start, start + 10):
            item = discount[i]
            if item in discount_dict:
                discount_dict[item] += 1
            else:
                discount_dict[item] = 1

        # 내가 원하는 상품 구성과 완전히 같은지 확인
        if discount_dict == want_dict:
            answer += 1

    return answer

## https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    clothes_dict = {}

    # 의상 종류별 개수 세기
    for name, kind in clothes:
        if kind not in clothes_dict:
            clothes_dict[kind] = 1
        else:
            clothes_dict[kind] += 1

    # 경우의 수 계산
    answer = 1
    for kind in clothes_dict:
        answer *= (clothes_dict[kind] + 1)

    # 아무것도 안 입은 경우 제거
    return answer - 1

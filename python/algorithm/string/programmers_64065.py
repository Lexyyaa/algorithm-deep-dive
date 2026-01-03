## https://school.programmers.co.kr/learn/courses/30/lessons/64065

import re

def solution(s):
    # 1) s에서 { ... } 형태의 "집합 내용"만 뽑아온다.
    # 예: "{{2},{2,1},{2,1,3}}" -> ["2", "2,1", "2,1,3"]
    parts = re.findall(r"\{([\d,]+)\}", s)

    # 2) 각 집합 문자열을 정수 리스트로 변환
    sets_list = []
    for p in parts:
        nums = list(map(int, p.split(',')))
        sets_list.append(nums)

    # 3) 집합을 길이(원소 개수) 기준으로 오름차순 정렬
    # 가장 작은 집합부터 보면, 매 단계마다 "새 원소"가 딱 1개씩 추가되는 구조
    sets_list.sort(key=len)

    answer = []
    seen = set()  # 지금까지 튜플에 들어간 원소들

    # 4) 작은 집합부터 순회하면서, 아직 안 나온 원소를 찾아 추가
    for group in sets_list:
        for x in group:
            if x not in seen:
                answer.append(x)
                seen.add(x)
                # 이 문제 구조상 매 그룹마다 새 원소는 1개만 추가됨
                break

    return answer

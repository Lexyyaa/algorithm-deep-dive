
### https://school.programmers.co.kr/learn/courses/30/lessons/64065


def solution(s):
    # "{{2},{2,1},{2,1,3}}" 같은 형태라서
    # 바깥의 "{{" 와 "}}" 떼고, "},{" 기준으로 쪼개면 각 집합 문자열이 됨
    groups = s[2:-2].split("},{")

    # 각 집합을 숫자 리스트로 변환
    sets_as_lists = [list(map(int, g.split(","))) for g in groups]

    # 원소 개수 작은 집합부터 보면, 매번 "새 원소 1개"가 추가되는 구조
    sets_as_lists.sort(key=len)

    seen = set()
    ans = []

    for group in sets_as_lists:
        for x in group:
            if x not in seen:
                # 이전에 없던 애가 이번에 새로 추가된 원소
                ans.append(x)
                seen.add(x)

    return ans

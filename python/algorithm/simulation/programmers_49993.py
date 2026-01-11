## https://school.programmers.co.kr/learn/courses/30/lessons/49993

def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        # tree에서 skill에 포함된 문자만 순서대로 남김
        filtered = ''.join(ch for ch in tree if ch in skill)

        # 남은 순서가 skill의 "앞에서부터" 일치하면 유효
        if skill.startswith(filtered):
            answer += 1

    return answer

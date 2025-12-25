## https://school.programmers.co.kr/learn/courses/30/lessons/12981

"""
이미 나온단어를 말하지않아야한다 -> set
이 조건을 필두로 번호와 차례를 구해주면되는 간단한문제!


"""
def solution(n, words):
    used = set()
    prev = words[0]
    used.add(prev)

    for i in range(1, len(words)):
        word = words[i]

        # 1) 끝말잇기 규칙 위반 (첫 글자 != 이전 단어의 마지막 글자)
        if word[0] != prev[-1]:
            player = (i % n) + 1
            turn = (i // n) + 1
            return [player, turn]

        # 2) 중복 단어 말함
        if word in used:
            player = (i % n) + 1
            turn = (i // n) + 1
            return [player, turn]

        used.add(word)
        prev = word

    return [0, 0]

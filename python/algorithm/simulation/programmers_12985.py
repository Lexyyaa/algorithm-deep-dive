## https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n, a, b):
    # 몇 번째 라운드인지 세기 위한 변수
    round_count = 0

    # a와 b가 아직 같은 번호가 아니라면
    # → 아직 서로 만나지 않았다는 뜻
    while a != b:

        # 현재 라운드에서 다음 라운드로 올라가면
        # 두 명씩 묶이므로 번호가 절반으로 줄어든다
        #
        # 1, 2 → 1
        # 3, 4 → 2
        # 5, 6 → 3
        # 7, 8 → 4
        #
        # 이 규칙을 수식으로 쓰면 (번호 + 1) // 2
        a = (a + 1) // 2
        b = (b + 1) // 2

        # 한 라운드를 진행했으므로 +1
        round_count += 1

        # 여기까지가 "한 라운드 진행"을 의미함
        # a와 b가 같은 번호가 되면
        # → 같은 경기에서 만난 것

    # while 문을 빠져나왔다는 것은
    # a == b 가 되었다는 뜻
    # 즉, 이 라운드에서 둘이 만남
    return round_count

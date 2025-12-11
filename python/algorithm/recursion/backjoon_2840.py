## https://www.acmicpc.net/problem/2840

import sys

# N = 5
# K = 6

# hint =[[1, 'A'], [2, 'B'], [5, 'B'], [1, 'C'], [2, 'A'], [2, 'B']]

## 문제에서 첫번째 줄에 마지막 회전에서 화살표가 가리키는 문자부터 시계방향으로 적어놓은 알파벳을 출력하라고 했으니까
## 우리는 마지막글자부터 역추적하면 되겠군!

# 입력 받기
N, K = map(int, sys.stdin.readline().split())
hint = []

for _ in range(K):
    move, ch = sys.stdin.readline().split()
    hint.append([int(move), ch])

wheel = ['?'] * N
now_char = hint[-1][1] ## 마지막 힌트로 바퀴에 문자 넣어주기
pos = 0
wheel[pos] = now_char

# 중복체크를 위한 set
used = set()
used.add(now_char)

for idx in range(K-1,0,-1): # 시작값, 끝값(포함안됨), 증감값(음수면 감소)

    move = hint[idx][0]
    char = hint[idx-1][1]
    pos = (pos + (move % N)) % N # 반시계방향 이동 (음수가 나올 수 있으니까 % N 한번 더 해줌)

    if wheel[pos] == '?': ## 빈칸인데
        if char in used: ## 넣으려고하는 문자가 이미 사용된 문자면 모순
            print('!')
            sys.exit(0)
        else:
            wheel[pos] = char
            used.add(char)
    else: ## 빈칸이 아닌데
        if wheel[pos] != char: ## 넣으려고하는 문자랑 다르면 모순
            print('!')
            sys.exit(0)

print(''.join(wheel))

"""
    나는 문제에서 
    현재 화살표는 idx 0 이니까 
    이전상태를 구하려면 move가 반시계(-move)로 이동해야한다는 논리를 갖고있었음 
    하지만 이 문제에서 바뀌는것은 "바퀴" 이지 "화살표" 가아님! 
    
    즉 화살표는 항상 idx 0 을 가리키고있고
    바퀴가 움직이는 것임!!
    
    따라서 이전상태를 구하려면 move가 시계(+move)로 이동해야함!!
"""






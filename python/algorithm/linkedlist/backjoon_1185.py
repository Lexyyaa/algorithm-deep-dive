n,k = map(int,input().split())
numbers = [n for n in range(1,n+1)] # 받은숫자 기반으로 배열만들기!
now_index = 0 # 시작점은 0번째 인덱스부터
result = [] # 결과를 담을 리스트


while numbers :
    now_index = now_index + k -1
    list_size = len(numbers)
    if now_index >= list_size :
        now_index %= list_size
    now_node = numbers[now_index]
    result.append(now_node) # 결과에 추가
    # result에 넣었으니까 이제 삭제함
    del numbers[now_index]

print("<",", ".join(result),">")
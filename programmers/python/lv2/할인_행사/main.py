def solution(want, number, discount):
    base_want_number_array = {}
    want_number_array = [{} for _ in range(100000)]
    
    for i in range(len(want)):
        base_want_number_array[want[i]] = number[i]
        
    for i in range(len(discount)):
        for j in range(10):
            if i - j >= 0:
                want_number_array[i-j][discount[i]] = want_number_array[i-j].get(discount[i], 0) + 1
    
    answer = 0
    for i in range(len(discount)):
        if base_want_number_array == want_number_array[i]:
            answer += 1
        
    return answer
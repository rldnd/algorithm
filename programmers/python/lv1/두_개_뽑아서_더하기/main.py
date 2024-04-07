def get_combinations(arr: list, length: int):
    result = []
    if length == 1:
        return list(map(lambda item: [item], arr))
    
    for index, item in enumerate(arr):
        rest = arr[index + 1:]
        combinations = get_combinations(rest, length - 1)
        attached = list(map(lambda combs: [item,*combs],combinations))
        result = [*result, *attached]
    return result

def solution(numbers):
    combinations = get_combinations(numbers, 2)
    summations = map(lambda item: item[0] + item[1],combinations)
    remove_duplicated_list = list(set(summations))
    remove_duplicated_list.sort()
    return remove_duplicated_list
    
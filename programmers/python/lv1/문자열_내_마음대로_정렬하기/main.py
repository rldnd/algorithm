def solution(strings, n):
    strings.sort(key = lambda item: (item[n], item))
    return strings
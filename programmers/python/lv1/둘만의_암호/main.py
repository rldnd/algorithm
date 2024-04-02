alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def solution(s, skip, index):
    for skip_char in skip:
        alphabets.remove(skip_char)

    result = ""
    for s_char in s:
        alphabet_index = alphabets.index(s_char)
        result += alphabets[(alphabet_index + index) % len(alphabets)]
        
    return result
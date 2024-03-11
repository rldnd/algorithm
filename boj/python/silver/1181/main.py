def bubble_sort_with_dictionary_order(lst: list):
    length = len(lst) - 1
    for i in range(length - 1):
        for j in range(length - i):
            if len(lst[j]) > len(lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
            if len(lst[j]) == len(lst[j+1]) and lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                
    return lst
    
N = int(input())
words = []
for _ in range(N):
    words.append(str(input()))

remove_duplicated_list = list(set(words))
short_order_list = bubble_sort_with_dictionary_order(words)

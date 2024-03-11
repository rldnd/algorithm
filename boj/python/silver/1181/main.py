N = int(input())
words = []
for _ in range(N):
    words.append(str(input()))


remove_duplicated_list = list(set(words))
remove_duplicated_list.sort(key = lambda x: (len(x), x))
for word in remove_duplicated_list:
    print(word)
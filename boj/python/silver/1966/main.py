import sys
readline = sys.stdin.readline
    
def get_queue_output():
    _, order = map(int, readline().split())
    docs = list(map(int, readline().split()))
    out_count = 0
    max_value = max(docs)
    
    while order != -1 and len(docs) > 0:
        if docs[0] == max_value:
            docs.pop(0)
            out_count += 1
            order -= 1
            if len(docs) > 0:
                max_value = max(docs) 
        elif docs[0] != max_value and order == 0:
            docs.append(docs.pop(0))
            order = len(docs) - 1
        else:
            docs.append(docs.pop(0))
            order -= 1
            
    print(out_count)

case_count = int(readline().rstrip())
for _ in range(case_count):
    get_queue_output()
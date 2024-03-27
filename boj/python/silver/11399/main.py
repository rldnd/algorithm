import sys
readline = sys.stdin.readline

person_count = int(readline())
times = list(map(int, readline().split()))
times.sort()
times.insert(0,0)
sum_times = [0] * (person_count + 1)
time = 0

for i in range(1, person_count + 1):
    sum_times[i] = times[i] + sum_times[i - 1]

for sum_time in sum_times[1:]:
    time += sum_time
    
print(time)
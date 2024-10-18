import sys
input = sys.stdin.readline

def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

n = int(input())
part_time = []
for i in range(n):
    interview_time = list(map(int, input().split()))
    part_time.append(sum(interview_time[1:]))

part_time = quick_sort(part_time)

sum_value = 0
prefix_sum = [0]
for i in part_time:
    sum_value += i
    prefix_sum.append(sum_value)

result = 0
for i in prefix_sum:
    result += i

print(result)
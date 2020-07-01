#퀵 정렬
import random

#########pivot을 잘 뽑는 것이 중요
def pivot_method(arr):
    return random.choice(arr)
################################

def quick(arr, pivot_method):
    if(len(arr) ==0):
        return arr
    
    pivot = pivot_method(arr)
    less = []
    more = []
    mid = []
    
    for i in arr:
        if i > pivot:
            more.append(i)
        elif i < pivot:
            less.append(i)
        else:
            mid.append(i)
    return quick(less, pivot_method) + mid + quick(more, pivot_method)

quick([3,2,10,7,5], pivot_method)

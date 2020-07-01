# 버블정렬

import matplotlib.pyplot as plt

arr = [10, 9, 11, 7, 5, 2, 6]
length = len(arr)

plt.bar(list(range(len(arr))), arr)
plt.show()
for j in range(length):
    for i in range(length-j-1):
        
        if( arr[i] > arr[i+1] ):
            arr[i], arr[i+1] = arr[i+1], arr[i]
    
    plt.bar(list(range(len(arr))), arr)
    plt.show()

arr

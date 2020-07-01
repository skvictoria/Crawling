# 삽입정렬

import matplotlib.pyplot as plt

arr = [3,2,10,7,5]
length = len(arr)

plt.bar(list(range(len(arr))), arr)
plt.show()
for j in range(length):
    for i in range(j, 0, -1):
        
        if( arr[i] < arr[i-1] ):
            arr[i], arr[i-1] = arr[i-1], arr[i]
    
    plt.bar(list(range(len(arr))), arr)
    plt.show()

arr

import matplotlib.pyplot as plt

#선택정렬 - 2중 for문과 big O 표기법 상 시간 같음.

arr = [10, 9, 11, 7, 5, 2, 6]
length = len(arr)

plt.bar(list(range(len(arr))), arr)
plt.show()
for j in range(length - 1):
    minimum = j
    for i in range(j,length):
        if( arr[minimum] < arr[i] ):
            minimum = i
    arr[minimum], arr[j] = arr[j], arr[minimum]
    plt.bar(list(range(len(arr))), arr)
    plt.show()

arr

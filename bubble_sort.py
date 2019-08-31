# Bubble Sort Algorithm Implementition

def bubbleSort(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

# calling the function
array = [9,8,7,6,5,4,3,2,1]
bubbleSort(array)
for i in range(len(array)):
    print(array[i])

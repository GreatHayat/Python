# Selection Sort Algorithm Implementition

def selectionSort(array):
    n = len(array)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

# Calling the function

array = [9,8,7,6,5,4,3,2,1]
selectionSort(array)
for i in range(len(array)):
    print(array[i])

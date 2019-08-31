# Insertion Sort Algorithm

def insertionSort(array):
    n = len(array)

    for i in range(1, n):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


# Calling the function
array = [5,4,3,2,1]
insertionSort(array)
for i in range(len(array)):
    print(array[i])

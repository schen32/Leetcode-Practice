def QuickSort(array):
    if len(array) <= 1:
        return array
    pivot = array[-1]
    i = -1
    for j in range(len(array)):
        if array[j] < pivot:
            i += 1
            temp = array[j]
            array[j] = array[i]
            array[i] = temp
    i += 1
    array[-1] = array[i]
    array[i] = pivot

    leftArray = QuickSort(array[0:i])
    rightArray = QuickSort(array[i+1:len(array)+1])
    array = leftArray + [pivot] + rightArray
    return array

test = [8,2,5,3,9,4,7,6,1]
test = QuickSort(test)
print(test)
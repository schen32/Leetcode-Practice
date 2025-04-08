def binarySearch(array, query):
    
    if not array:
        return -1
    middleIndex = len(array)//2
    middleValue = array[middleIndex]
    
    if middleValue == query:
        return middleIndex
    elif middleValue < query:
        return binarySearch(array[0:middleIndex], query)
    else:
        return binarySearch(array[middleIndex+1:len(array)+1], query)


test = [13,11,10,7,4,3,1,0]
index = binarySearch(test, 1)
print(index)
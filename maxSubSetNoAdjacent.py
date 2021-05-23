def maxSubsetSumNoAdjacent(array):
    if not len(array):
        return
    elif len(array) == 1:
        return array[0]
    first = max(array[0],array[1])
    second = array[0]
    for i in range(2,len(array)):
        current = max(first,second+array[i])
        second = first
        first = current
    return current

maxSubsetSumNoAdjacent([5,5,10,100,10,5])
    

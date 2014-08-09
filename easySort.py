def easySortIter(L):
    for i in range(len(L)):
        minIndex = i
        minValue = L[i]

        j = i + 1
        while j < len(L):
            if minValue > L[j]:
                minValue = L[j]
                minIndex = j

            j += 1

        temp = L[i]
        L[i] = minValue
        L[minIndex] = temp


    return L


def easySortRec(L):
    if len(L) == 1:
        return L
    else:
        newL = smallest(L)
        return  [newL[0]] + easySortRec(newL[1:])


def smallest(L):
    minIndex = 0
    minValue = L[0]

    j = 1
    while j < len(L):
        if minValue > L[j]:
            minIndex = j
            minValue = L[j]
        j += 1

    temp = L[0]
    L[0] = minValue
    L[minIndex] = temp
    return L

def divSort(L, low , high):
    if low >= high:
        return L
    else:
        middle = sqlit(L, low, high)
        divSort(L, 0, middle - 1)
        divSort(L, middle + 1, high)
    return L

def sqlit(L, low , high):
    #middle = low + (high - low) / 2
    middle = low
    port = L[middle]
    

    while True:
        while L[high] >= port and low < high:
            high -= 1

        if low >= high:
            break
    
        L[low] = L[high]
        low += 1
        
        while L[low] <= port and low < high:
            low += 1
        if low >= high:
            break
        L[high] = L[low]
        high -= 1

        



    L[high] = port

    return high

import operator
def mergeSort(L, compare = operator.lt):
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left =  mergeSort(L[:middle], compare)
        right =  mergeSort(L[middle:], compare)
        return merge(left, right, compare)

def merge(left, right, compare):
    i, j = 0, 0
    new = []
    while i < len(left) and j < len(right):
        if compare(left[i], right[j]):
            new.append(left[i])
            i += 1
        else:
            new.append(right[j])
            j += 1

    while i < len(left):
        new.append(left[i])
        i += 1

    while j < len(right):
        new.append(right[j])
        j += 1
    print('left:' + str(left) + ' right:' + str(right) + ' new: '+ str(new))
    return new

        

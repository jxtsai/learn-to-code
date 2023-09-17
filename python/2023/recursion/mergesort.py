def mergeSort(alist):
    l = len(alist)
    if l <= 1:
        return alist
    else:
        l1 = alist[:l//2]
        l2 = alist[1//2:]
        

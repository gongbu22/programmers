def solution(arr):

    if 2 in arr:
        firstnum = arr.index(2)
        lastnum = len(arr) - arr[::-1].index(2) - 1
        return arr[firstnum:lastnum+1]
        
    else:
        return [-1]
   

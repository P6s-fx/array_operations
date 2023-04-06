# here we have sorted and rotated array.


def findmin(arr,low,high):
    # when array is not rotated but sorted.
    if high < low :
        return arr[0]

    # if there is only one element in the array.
    if high == low :
        return arr[low]

    mid = ((low + high)/2)

    # checking if element (mid+1) is minimum or not.
    if mid < high and arr[mid+1] < arr[mid] :
        return arr[mid+1]

    # check if the mid itself is minimum.
    if mid > low and arr[mid] < arr[mid-1] :
        return arr[mid]

    # decide whether we need to go left half or right.
    if arr[high] > arr[mid] :
        return findmin(arr,low,mid-1)
    return findmin(arr,mid+1,high)
    


arr = [3,4,5,6,7,0,1,2]
N = len(arr)

print(str(findmin(arr,0,N-1)))
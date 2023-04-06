def ins_elem(arr,n,x,pos):

    arr = arr.insert(pos,x)
    # for i in range(n-1,pos,-1):
    #     arr[i+1] = arr[i]

    # i = n-1
    # while i >= pos :
    #     arr[i+1] = arr[i]
    #     i -= 1
    # arr[pos] = x

arr = [4,5,7,11,2,9]
n = 7
x=10
pos = 3

ins_elem(arr,n,x,pos)

for i in arr:
    print(i)
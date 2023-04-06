# Complexity --> O(N)


def rotate(ar, d, N):
    k = ar.index(d)
    new_lis = []
    new_lis = ar[k+1:]+ar[0:k+1]
    return new_lis
 
 
# if __name__ == '__main__':
#     arr = [1, 2, 3, 4, 5, 6, 7]
#     d = 2
#     N = len(arr)
N = int(input("enter array size : "))
arr = [0] * N
for i in range(N):
    arr[i] = input(f"Enter {i}th element : ")


d = input("enter rotation index : ")
print(arr)

# Function call
arr = rotate(arr, d, N)
for i in arr:
    print(i)



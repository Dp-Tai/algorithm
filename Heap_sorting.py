


# build max heap tree
def Max_heap(arr,n,index):
    max_index = index
    left = 2*index + 1
    right = 2*index +2
    if left < n and arr[left] > arr[max_index]:
        max_index = left
    if right < n and arr[right] > arr[max_index]:
        max_index = right
    if max_index != index:
        arr[index],arr[max_index] = arr[max_index],arr[index]
        Max_heap(arr,n,max_index)

# call for max heap sorting
def Heap_Sorting(arr):
    for i in range(len(arr),-1,-1): 
        Max_heap(arr,len(arr),i)
        
    for i in range(len(arr)-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        Max_heap(arr,i,0)
    return arr

        
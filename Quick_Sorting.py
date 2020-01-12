
def Pivot(arr,low,high):
    pi = arr[high]
    index = low - 1
    for j_index in range(low,high):
        if arr[j_index] < pi:
            index = index + 1
            arr[index], arr[j_index] = arr[j_index],arr[index]
    arr[index + 1],arr[high] = arr[high],arr[index + 1]
    return index + 1 

def Quick_Sort(arr,low,high):
    if low < high:
        pivot = Pivot(arr,low,high)
        Quick_Sort(arr,low,pivot-1)
        Quick_Sort(arr,pivot+1,high)
    return arr



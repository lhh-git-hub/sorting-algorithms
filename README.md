# sorting-algorithms
十大排序算法
#冒泡排序
def bubble_sort(arr):
    r=len(arr)
    swap = True   #做标记
    for i in range(r-1):    #若是上一轮没有交换，就说明已经有序，退出
        if not swap:
            break
        swap = False  #每一轮循环前把swap标记为False
        for j in range(r-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swap=True
    return arr

#选择排序
def selection_sort(arr):
	n=len(arr)
	for i in range(n):
		mindx=i
		for j in range(i+1,n):
			if arr[j] < arr[mindx]:
				mindx=j
		arr[i],arr[mindx]=arr[mindx],arr[i]
		return arr


#插入排序
def insert_sort(arr)
	n = len(arr)
	for i in range(1,n): #初始数组的第一个元素为有序数组
		key = arr[i]
		if key > arr[i-1]  #若标记元素大于已排序的最后一则提前退出
			continue
		j = j-1  #标记元素前一个元素，即有序部分最后一个元素
		while j >= 0 and key < arr[j]: #从有序部分的最后一个元素进行比较
			arr[j+1] = arr[j]  #若key小于该元素，则将该元素向后移一位，空出当前位置
			j -= 1
		arr[j+1] = key #就像它要移到数组的第一个位置，j此时=-1，则j+1 才是数组的首元素下标
	return arr

#快速排序
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    key = arr[len(arr)//2]
    left = [x for x in arr if x < key]
    mid = [x for x in arr if x == key]
    right = [x for x in arr if x > key]
    return quick_sort(left)+quick_sort(mid)+quick_sort(right)

#归并排序
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

#堆排序
	
def heap_sort(arr):
    n = len(arr)
    
    # 构建最大堆
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # 逐个提取堆顶元素并调整堆
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 将堆顶元素（最大值）与最后一个元素交换
        heapify(arr, i, 0)  # 调整堆，使其重新满足最大堆的性质
    return arr

def heapify(arr, n, i):
    largest = i  # 初始化最大值的索引
    left = 2 * i + 1  # 左子节点
    right = 2 * i + 2  # 右子节点
    
    # 如果左子节点存在且大于当前最大值
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    # 如果右子节点存在且大于当前最大值
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    # 如果最大值不是当前节点，交换并递归调整
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


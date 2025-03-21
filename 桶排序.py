def bucket_sort(arr):
    # 1. 创建桶
    n = len(arr)
    buckets = [[] for _ in range(n)]

    # 2. 将元素分配到桶中
    for num in arr:
        index = int(n * num)  # 计算元素应该放入哪个桶
        buckets[index].append(num)

    # 3. 对每个桶中的元素进行排序（这里使用内置的排序函数）
    for bucket in buckets:
        bucket.sort()

    # 4. 将所有桶中的元素依次取出，得到有序序列
    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(bucket)

    return sorted_arr



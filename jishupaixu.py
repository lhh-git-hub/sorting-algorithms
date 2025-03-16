def radix_sort(arr):
    # 找到最大数，确定位数
    max_num = max(arr)
    digit = len(str(max_num))

    # 从最低位到最高位进行排序
    for i in range(digit):
        # 初始化桶
        buckets = [[] for _ in range(10)]
        # 将元素放入对应的桶中
        for num in arr:
            bucket_index = (num // 10**i) % 10
            buckets[bucket_index].append(num)
        # 按顺序收集桶中的元素
        arr = [num for bucket in buckets for num in bucket]

    return arr


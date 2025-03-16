def counting_sort(arr):
    # 找到数组中的最大值和最小值
    max_val = max(arr)
    min_val = min(arr)
    # 计算计数数组的长度
    range_of_elements = max_val - min_val + 1
    # 初始化计数数组
    count = [0] * range_of_elements
    # 初始化输出数组
    output = [0] * len(arr)

    # 统计每个元素出现的次数
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1

    # 计算累积计数
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 构建输出数组
    i = len(arr) - 1
    while i >= 0:
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
        i -= 1

    # 将输出数组复制回原数组
    for i in range(len(arr)):
        arr[i] = output[i]

    return arr




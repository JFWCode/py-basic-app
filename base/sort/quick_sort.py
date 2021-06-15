

def quick_sort(arr, start=None, end=None):
    if start is None or end is None or \
            not start < end:
        return

    i = start
    j = end
    base = arr[start]

    while i < j:
        # 注意顺序，必须从右边开始
        while arr[j] >= base and i < j:
            j -= 1

        while arr[i] <= base and i < j:
            i += 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[start] = arr[i]
    arr[i] = base

    quick_sort(arr, start, i - 1)
    quick_sort(arr, i + 1, end)


if __name__ == '__main__':
    arr = [12, 213, 32, 324, 21, 2, 2, 0]

    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
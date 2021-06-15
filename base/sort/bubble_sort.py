def bubble_sort(arr: list) -> list:
    n = len(arr)

    for i in range(0, n):

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    arr = [12, 213, 32, 324, 21, 2, 2, 0]

    print(bubble_sort(arr))

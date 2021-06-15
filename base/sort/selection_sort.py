from base.sort import Sort


class SelectionSort(Sort):
    @classmethod
    def sort(cls, arr):
        n = len(arr)

        for i in range(0, n):
            min_index = i

            for j in range(i + 1, n):
                if arr[min_index] > arr[j]:
                    min_index = j

            if min_index != i:
                arr[min_index], arr[i] = arr[i], arr[min_index]

        return arr


if __name__ == '__main__':
    arr = [12, 213, 32, 324, 21, 2, 2, 0]
    print(getattr(SelectionSort, 'sort')(arr))
    # print(SelectionSort.sort(arr))

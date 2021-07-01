
def test(n):
    ll = []
    for i in n:
        if isinstance(i, list):
            ll.extend(test(i))
        else:
            ll.append(i)
    return ll


if __name__ == '__main__':
    n = [1, 2, [3, [4, [5, 6], 7], 8], 9]
    after = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = test(n)
    print(result)
    assert result == after

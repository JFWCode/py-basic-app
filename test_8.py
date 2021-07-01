
def test(n):
    result = []

    if n % 3 == 0:
        result.append('zhong')
    if n % 5 == 0:
        result.append('guo')
    if n % 7 == 0:
        result.append('ren')

    if len(result) == 0:
        result.append(n)

    return result


if __name__ == '__main__':
    n = 105
    print(test(n))
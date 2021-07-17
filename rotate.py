from utils.time_watch import time_watch

class Rotate:
    ''' 数组循环左移
    '''
    @classmethod
    def fun_1(cls, lst, k):
        tmp = lst[:]
        print(id(tmp))
        print(id(lst))

        for i in range(k):
            tmp.append(tmp.pop(0))
        return tmp

    @classmethod
    def fun_2(cls, lst, k):
        m = k % len(lst)
        return lst[m:] + lst[:m]

    # 暴力循环
    @classmethod
    def fun_3(cls, lst, k):
        m = k % len(lst)

        for i in range(m):
            tmp = lst[0]
            for j in range(1, len(lst)):
                lst[j-1] = lst[j]
            lst[-1] = tmp

        return lst

@time_watch
def test(s):
    res = Rotate.fun_1(s, 17)
    return res


if __name__ == '__main__':
    s = [1, 4, 53, 32, 2, 13, 22]
    res = test(s)
    print(res)

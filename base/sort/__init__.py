import abc


class Sort:
    @classmethod
    @abc.abstractmethod
    def sort(cls, arr):
        pass


class A:
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        super(B, self).__init__()
        print('B')


if __name__ == '__main__':
    B()
    print(type(A) == type(B))

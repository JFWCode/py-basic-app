import threading


def singleton(cls):
    _instance = {}

    def _singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton

@singleton
class Foo:
    def __init__(self, val):
        pass


class Singleton:
    _thread_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._thread_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = object.__new__(cls)

        return cls._instance



if __name__ == '__main__':

    # f1 = Foo(1)
    # f2 = Foo(2)
    #
    # print(f1)
    # print(f1.val)
    # print(f2)
    # print(f1.val)
    # print(f2.val)

    s1 = Singleton()
    s2 = Singleton()
    print(s1)
    print(s2)

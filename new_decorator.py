# 接收正整型n,捕捉被装饰函数的异常，若有异常则进行重试，最多重试n次，第n次打印异常信息
from functools import wraps


def decorate(func):
    @wraps(func)
    def _wrapper(n):
        print(func.__name__)
        while n > 1:
            try:
                func(n)
            except Exception as e:
                pass
            else:
                break

            n -= 1

        if n == 1:
            try:
                func(n)
            except Exception as e:
                print(str(e))

    return _wrapper


def cache(time):
    def inner(func):
        def _wrapper(*args, **kwargs):
            print(time)
            return func(*args, **kwargs)

        return _wrapper
    return inner


@cache(5)
@decorate
def foo(val):
    print(val)
    raise Exception('error')


if __name__ == '__main__':
    foo(3)

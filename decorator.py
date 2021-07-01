import functools


def decorator(func):
    content = "I'm decorator"

    @functools.wraps(func)
    def _wrapper(*args, **kwargs):
        print(content)
        print(func.__name__)
        print(func.__doc__)
        func(*args, **kwargs)

    return _wrapper


def add_params(params):
    print(params)

    def c_decorator(func):
        content = "I'm decorator"

        def _wrapper(*args, **kwargs):
            print(content)
            print(func.__name__)
            print(func.__doc__)
            return func(*args, **kwargs)

        return _wrapper

    return c_decorator


#@add_params('hi')
def test(val):
    '''
    test
    :param val: Integer
    :return:
    '''
    print(val)
    return "gg"


if __name__ == '__main__':
    print(add_params('call')(test)(11))
from functools import wraps

def decorator_with_params(val):
    print(val)
    def decorator(func):
        @wraps(func)
        def _wrap(*args, **kwargs):
            print(111)
            func(*args)
            print(222)
        return _wrap
    return decorator

@decorator_with_params('hi')
def demo(obj):
    print('demo')
    # if isinstance(obj, dict) or isinstance(obj, list):
    #     for i in obj:
    #         demo(i)
    #
    # if not obj:
    #     obj.pop()


if __name__ == '__main__':
    s = {'s1': [], 's2': {'s3': 2, 's4': ' '}, 's5': 12}

    demo(s)
    print(s)






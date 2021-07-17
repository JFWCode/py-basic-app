import time


def time_watch(func):

    def _wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print('use time: %.8f' % (end_time - start_time))
        return  res

    return _wrapper

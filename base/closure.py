
def make_averager():
    s = []

    def averager(var):
        s.append(var)
        total = sum(s)/len(s)
        print(s)
        print(total)
    return averager


if __name__ == '__main__':
    avg = make_averager()
    avg(1)
    avg(1)
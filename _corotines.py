def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


def sub_gen():
    x = 'ready to accept message'
    message = yield x
    print(f'received: {message}')


@coroutine
def avg():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)

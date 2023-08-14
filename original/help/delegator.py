def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


def sub_gen():
    while True:
        try:
            message = yield
        except StopIteration:
            break
        else:
            print(f'Message: {message}')

    return 'Returned from sub_gen()'


@coroutine
def delegator(g):
    result = yield from g
    print(result)

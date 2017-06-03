import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('before call %s():' % func.__name__)
        func(*args, **kw)
        print('after call %s():' % func.__name__)
    return wrapper

@log
def now():
    print('2017-6-1')
    return 'I like it.'

print(now())

def consumer():
    r = ''
    while True:
        student = yield r
        if not student:
            return
        print('[CONSUMER] Consuming %s...' % student)
        r = '200 OK'

def produce(c):
    r1 = c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
produce(c)
class Rack(object):
    def __init__(self, capacity):
        self._balls = [0 for _ in xrange(capacity)]
        self._index = lambda x: x
        self._deIndex = lambda x: x

    def balls(self):
        y = filter(lambda t: t[1]>0,enumerate(self._balls))
        z = map(lambda t: [self._deIndex(t[0]) for _ in xrange(t[1])], y)
        return list(reduce(lambda p,n: p+n,z,[]))

    def add(self, item):
        self._balls[self._index(item)]+=1

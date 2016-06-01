class HeffAssess(object):
    def __init__(self):
        self._capacity = 26
        self._index = lambda x: ord(x.lower())-97
        self._deIndex = lambda x: chr(97+x)

    def _tidyReducer(self,x,y):
        x[y]+=1
        return x

    def assess(self,input):
        a = reduce(self._tidyReducer,filter(lambda x: -1<x<26, map(lambda x:self._index(x),input)),[0 for _ in xrange(self._capacity)])
        b = filter(lambda t: t[1]>0,enumerate(a))
        print b
        return ''.join([self._deIndex(i)*c for i,c in b])

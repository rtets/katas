class LowerCaseNoPuncSummariser(object):
    def summarise(self,word):
        s = filter(lambda x: 96 < ord(x) < 123,list(word.lower()))
        s.sort()
        return str.join('',s)

class BothCaseNoPuncSummariser(object):
    def summarise(self,word):
        s = filter(lambda x: 96 < ord(x) < 123 or 64 < ord(x) < 91,list(word))
        s.sort()
        return str.join('',s)

class BothCasePlusPuncSummariser(object):
    def summarise(self,word):
        s = list(word)
        s.sort()
        return str.join('',s)

class Finder(object):
    def __init__(self,summy = LowerCaseNoPuncSummariser()):
        self.foo = 'bar'
        self.summy = summy

    def find(self,words):
        anas = dict()
        for word in words:
            e = self.summy.summarise(word)
            if e in anas:
                anas[e] += [word]
            else:
                anas[e] = [word]
        return anas

class Summary(object):
    def __init__(self):
        self.foo = 'bar'

import sys

from anagrams import Finder,BothCaseNoPuncSummariser,LowerCaseNoPuncSummariser,BothCasePlusPuncSummariser

def main(wordFile):
    with open(wordFile,'r') as fin:
        words = [word.rtrim('\n') for word in fin]
    f = Finder(BothCasePlusPuncSummariser())
    res = f.find(words)
    sets = [v for k,v in res.items() if len(v) > 1]
    setCount = len(sets)
    memberCount = reduce(lambda x,y: x+len(y), sets, 0)
    print 'found {1} sets of anagrams\nwith an aggregate {0} members'.format(memberCount,setCount)

if __name__ == '__main__':
    main(sys.argv[1])

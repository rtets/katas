import sys

class CodeLineFormatter(object):
    _OKGREEN = '\033[92m'
    _FAIL = '\033[91m'
    _ENDC = '\033[0m'

    @staticmethod
    def printNonCodeLine(output):
        print '{0}{1}{2}'.format(CodeLineFormatter._FAIL,output,CodeLineFormatter._ENDC)

    @staticmethod
    def printCodeLine(output):
        print '{0}{1}{2}'.format(CodeLineFormatter._OKGREEN,output,CodeLineFormatter._ENDC)


class Tokeniser(object):
    def __init__(self,tokens):
        self._tokens = {token for token in tokens}
        self._lengths = sorted({len(token) for token in tokens}, reverse=True)

    def tokenise(self,line):
        i, leftBound, linelen = 0, 0, len(line)
        if linelen>0:
            while i <= linelen:
                shiftDistance = 1
                for tokenLength in self._lengths:
                    if i+tokenLength<=linelen and line[i:i+tokenLength] in self._tokens:
                        if i>=leftBound:
                            yield line[leftBound:i]
                        yield line[i:i+tokenLength]
                        shiftDistance = tokenLength
                        leftBound = i + shiftDistance
                        break
                i+=shiftDistance
            if i>=leftBound:
                yield line[leftBound:linelen]


class JavaLineCounter(object):
    def __init__(self,formatter = None):
        self._singleLineComment = '//'
        self._multiLineCommentOpen = '/*'
        self._multiLineCommentClosed = '*/'
        self._stringLiteralOpenAndClosed = '"'
        self._tokeniser = Tokeniser({self._singleLineComment, self._multiLineCommentOpen, self._multiLineCommentClosed, self._stringLiteralOpenAndClosed})
        self._formatter = CodeLineFormatter if formatter==None else formatter


    def countCodeLines(self,input):
        openString, multiLineComment = False,False
        codeLines = 0
        for line in input:
            isCodeLine, leavesCommentOpen = self._evaluateLine(line,multiLineComment)
            if isCodeLine:
                codeLines+=1
                self._formatter.printCodeLine(' {1} {0}'.format(line, codeLines))
            else:
                self._formatter.printNonCodeLine(' - {0}'.format(line))
            multiLineComment = leavesCommentOpen
        print codeLines

    def _evaluateLine(self, line, existingCommentOpen):
        singleLineComment,stringLiteralOpen,isCodeLine = False,False,False
        tokens = self._tokeniser.tokenise(line)
        for token in tokens:
            if len(token.strip())>0:
                if existingCommentOpen:
                    if token == self._multiLineCommentClosed:
                        existingCommentOpen = False
                elif stringLiteralOpen:
                    if token == self._stringLiteralOpenAndClosed:
                        stringLiteralOpen = False
                else:
                    if token == self._multiLineCommentOpen:
                        existingCommentOpen = True
                    elif token == self._stringLiteralOpenAndClosed:
                        stringLiteralOpen = True
                    elif token == self._singleLineComment:
                        return (isCodeLine,existingCommentOpen)
                    else:
                        isCodeLine = True
        return (isCodeLine, existingCommentOpen)


def lineYieldify(filename):
    with open(filename,'r') as fin:
        for line in fin:
            yield line.rstrip('\n')

def main(filename):
    counter = JavaLineCounter()
    counter.countCodeLines(lineYieldify(filename))


if __name__ == '__main__':
    main(sys.argv[1])

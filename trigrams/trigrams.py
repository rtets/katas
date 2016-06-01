import sys
from random import randint

def randitem(collection):
    return collection[randint(0,len(collection)-1)]

def main(input,output):
    trigrams = dict()
    with open(input,'r') as fin:
        buffer = (None,None)
        for line in fin:
            if line==line.upper():
                #probably a chapter heading...
                continue
            for part in line.split():
                if buffer in trigrams:
                    trigrams[buffer].append(part)
                else:
                    trigrams[buffer] = [part]
                buffer = (buffer[1],part)

    for k in filter(lambda x:x[0]==None,trigrams.keys()):
        del trigrams[k]

    i=2
    buffer = randitem(trigrams.keys())
    with open(output,'w') as fout:
        fout.write('{0} {1}'.format(*buffer))
        sp,le = True,False
        while buffer in trigrams and i<10000:
            options = trigrams[buffer]
            part = randitem(options)
            fout.write(' {0}'.format(part))
            buffer = (buffer[1],part)
            i+=1
    print '{0} words written'.format(i)


if __name__ == '__main__':
    main(*sys.argv[1:])

import sys
from random import randint

def main(input,outout):
    trigrams = dict()
    with open(input,'r') as fin:
        buffer = (None,None)
        for line in fin:
            for part in line.split():
                if buffer in trigrams:
                    trigrams[buffer].append(part)
                else:
                    trigrams[buffer] = [part]


    i=0
    buffer = trigrams.keys[randint(len(trigrams))]
    with open(output,'w') as fout:
        fout.write('{0} {1}'.format(*buffer))
        while buffer in trigrams and i<1000:
            fout.write(' {0}'.format(part))
            buffer = (buffer[1],part)
            i+=1


if __name__ == '__main__':
    main(*sys.argv[1:])

import sys
import numpy as np

class Node(object):
    def __init__(self,number,parent):
        self._parent = parent
        self._number = number
        self._satisfied = number > 100 or number == 6 or np.sqrt(number) % 1 == 0
        self._left = None
        self._right = None
        self._depth = parent.depth + 1 if parent != None else 1

    @property
    def parent(self):
        return self._parent

    @property
    def number(self):
        return self._number

    @property
    def satisfied(self):
        return self._satisfied

    @property
    def depth(self):
        return self._depth

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self,value):
        self._left = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self,value):
        self._right = value

def print_all_chains(node,chain=[]):
    if node.left is None:
        chain.append(node.number)
        print '{0}: {1}'.format(node.satisfied, chain)
    else:
        print_all_chains(node.left, chain[:] + [node.number])
        print_all_chains(node.right, chain[:] + [node.number])

def build_tree(node, maxDepth):
    if not node.satisfied and node.depth<maxDepth:
        node.left = Node(node.number*2, node)
        build_tree(node.left,maxDepth)
        node.right = Node(node.number//3, node)
        build_tree(node.right,maxDepth)


def find_decay(number):
    root = Node(number,None)
    build_tree(root,maxDepth=10)
    print_all_chains(root)

if __name__ == '__main__':
    find_decay(int(raw_input('Number: ')))

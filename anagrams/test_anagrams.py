import unittest, sys, os
from anagrams import Finder

class TestFinder(unittest.TestCase):
    # def setUp(self):
    #     self.test_helper = TestHelper()
    #
    # def tearDown(self):
    #     self.test_helper.remove_working_files()

    def test_fewBeards(self):
        someWords = ['beard','bread','bared','breed','brada','brea','bear','bead']
        f = Finder()
        anas = f.find(someWords)
        self.assertEqual(['beard','bread','bared'],anas['abder'])


class TestHelper(object):
    def __init__(self):
        self.working_input_file = 'working_input'
        self.working_output_file = 'working_output'

    def remove_working_files(self):
        if os.path.exists(self.working_input_file):
            os.remove(self.working_input_file)
        if os.path.exists(self.working_output_file):
            os.remove(self.working_output_file)

    def swap_stdin_stdout(self,inputcontent):
        self.original_stdin,self.original_stdout = sys.stdin,sys.stdout
        with open(self.working_input_file,'w') as fout:
            fout.write('{0}{1}'.format(inputcontent,'' if inputcontent.endswith('\n') else '\n'))
        fin = open(self.working_input_file,'r')
        fout = open(self.working_output_file,'w')
        return fin,fout

    def unswap_stdin_stdout(self,outputcontent):
        sys.stdin.close()
        sys.stdout.close()
        sys.stdin, sys.stdout = self.original_stdin,self.original_stdout
        with open(self.working_output_file,'r') as fin:
            outputcontent += fin.readlines()

if __name__ == '__main__':
    unittest.main()

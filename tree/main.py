import sys
from antlr4 import *
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser

class algTree:
    def __init__(self):
        childs = []
 
    def visit(self, a):
        if a.__class__.__name__ == 'TerminalNodeImpl':
            if a.getText()=='<EOF>':
                print("end", end = "")
                return
            if a.getText()!='\n':
                print("(",a.getText(),")", end = "")
            return
        else:
            print('(', end = "")
            print(a.__class__.__name__, end = "")
            for i in a.children:
                self.visit(i)
            print(')', end = "")
            return
     

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()
    walker = algTree()
    walker.visit(tree)

main([None, "test.py"])


#if __name__ == '__main__':
#    main(sys.argv)

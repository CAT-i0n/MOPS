import sys
from antlr4 import *
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser


 
def visitor(a):
    if a.__class__.__name__ == 'TerminalNodeImpl':
        if a.getText()=='<EOF>':
            print("end")
            return
        if a.getText()!='\n':
            print("(",a.getText(),")")
        if a.getText()=='<EOF>':
            print("end")
        return
    else:
        print('(', end = "")
        #print(a.__class__.__name__, end = "")
        for i in a.children:
            visitor(i)
        print(')', end = "")
        return
    


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()
    print(dir(tree))
    visitor(tree)



if __name__ == '__main__':
    main(sys.argv)

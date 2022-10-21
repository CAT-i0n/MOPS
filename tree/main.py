import sys
from antlr4 import *
from Python3Lexer import Python3Lexer
from Python3Parser import Python3Parser


class algTree:
    def __init__(self, ast):
        self.ast = ast
        self.childs = []
        self.data_type = ''
        self.data = ''
    def visit(self):
        if self.data_type == 'TerminalNodeImpl':
            print(self.data)
            return
        else:
            print('(', end = "")
            print(self.data_type)
            for i in self.childs:
                i.visit()
            print(')', end = "")
            return
    def build(self):
        self.data_type = self.ast.__class__.__name__
        self.data = self.ast.getText()
        if self.ast.__class__.__name__ == 'TerminalNodeImpl':
            return
        else:
            for i in self.ast.children:
                child = algTree(i)
                child.build()
                self.childs.append(child)
            return
        


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()
    walker = algTree(tree)
    walker.build()
    walker.visit()
    

main([None, 'test.py'])


#if __name__ == '__main__':
#    main(sys.argv)

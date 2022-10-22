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
        if self.data_type == 'terminal':
            if self.data == '\n':
                return
            print(self.data, end = "")
            return
        else:
            print('(', end = "")
            print(self.data_type, end = "")
            for i in self.childs:
                i.visit()
            print(')', end = "")
            return
    def build(self, rules):
        self.data = self.ast.getText()
        if self.ast.__class__.__name__ == 'TerminalNodeImpl':
            self.data_type = 'terminal'
            return
        else:
            self.data_type = rules.ruleNames[self.ast.getRuleIndex()] 
            for i in self.ast.children:
                child = algTree(i)
                child.build(rules)
                self.childs.append(child)
            return
        


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()
    walker = algTree(tree)
    walker.build(parser)
    walker.visit()
    

project_path = 'test.py'
main([None, project_path])


#if __name__ == '__main__':
#    main(sys.argv)

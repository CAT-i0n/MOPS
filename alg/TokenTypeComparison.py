
from lib2to3.pgen2 import token
import sys
from antlr4 import *

from tree.Python3Lexer import Python3Lexer

class Match:

    def __init__(self):
        self.startFirst = 0
        self.startSecond = 0
        self.length = 0
    
    def overlaps(self, other):
        if self.startFirst < other.startFirst:
            if (other.startFirst - self.startFirst) < self.length:
                return True
        else:
            if (self.startFirst - other.startFirst) < other.length:
                return True

        if self.startSecond < other.startSecond:
            return (other.startSecond - self.startSecond) < self.length
        else:
            return (self.startSecond - other.startSecond) < other.length

    def __repr__(self) -> str:
        return f"Match({self.startFirst} {self.startSecond} {self.length})"

class ComparisonResult:

    def __init__(self, first, second, matchs: list[Match]):
        self.first = first
        self.second = second
        self.matchs = matchs

    def similarity(self) -> float:
        similarity = 0
        for i in range(len(self.matchs)):
            similarity += self.matchs[i].length

        similarityFirst = similarity / len(self.first)
        similaritySecond = similarity / len(self.second)

        return max(similarityFirst, similaritySecond)
        
def printComparisonReport(file1: str, file2: str, min_length = 4, SIZE = 100):
    tokens1 = getTokens(file1)
    tokens2 = getTokens(file2)
    result = comparison(tokens1, tokens2, min_length)

    def formatLine(s) -> str:
        s = str(s)
        l = min(len(s), SIZE)
        return s[0:l].ljust(SIZE, ' ')

    print('similarity: ', result.similarity())
    print('matchs: ', len(result.matchs))
    print(formatLine(file1), end='')
    print('|', end='')
    print(formatLine(file2))
    print('-' * SIZE, end='')
    print('|', end='')
    print('-' * SIZE)

    lines1 = ['']
    lines2 = ['']
    with open(file1) as f:
        lines1.extend(f.read().split('\n'))
    with open(file2) as f:
        lines2.extend(f.read().split('\n'))

    for m in result.matchs:
        line1 = range(tokens1[m.startFirst].line, tokens1[m.startFirst + m.length].line)
        line2 = range(tokens2[m.startSecond].line, tokens2[m.startSecond + m.length].line)

        for i in range(min(len(line1), len(line2))):
            print(formatLine('{}. {}'.format(line1[i], lines1[line1[i]])), end='')
            print('|', end='')
            print(formatLine('{}. {}'.format(line2[i], lines2[line2[i]])))

        if len(line1) > len(line2):
            for i in range(len(line2), len(line1)):
                print(formatLine('{}. {}'.format(line1[i], lines1[line1[i]])), end='')
                print('|', end='')
                print(formatLine(''))
        else:
            for i in range(len(line1), len(line2)):
                print(formatLine(''), end='')
                print('|', end='')
                print(formatLine('{}. {}'.format(line2[i], lines2[line2[i]])))
        
        print('-' * SIZE, end='')
        print('|', end='')
        print('-' * SIZE)

def getTokens(file: str) -> list[Token]:
    input_stream = FileStream(file)
    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.getNumberOfOnChannelTokens()
    return stream.tokens
    
def addMatchIfNotOverlapping(matchs: list[Match], match):
    over = []
    for m in matchs:
        if m.overlaps(match):
            over.append(m)
    sum = 0
    for m in over:
        sum += m.length
    if sum < match.length:
        for m in over:
            matchs.remove(m)
        matchs.append(match)

def comparison(first: list[Token], second: list[Token], min_line_length = 1) -> ComparisonResult:
    globalMatchs = []
    for startFirst in range(len(first)):
        for startSecond in range(len(second)):
            length = 0
            while first[startFirst + length].type == second[startSecond + length].type:
                if startSecond + length + 1 >= len(second):
                    break
                if startFirst + length + 1 >= len(first):
                    break
                length += 1
            lines1 = first [startFirst  + length].line - first [startFirst].line  + 1
            lines2 = second[startSecond + length].line - second[startSecond].line + 1
            if lines1 >=  min_line_length and lines2 >= min_line_length:
                m = Match()
                m.startFirst = startFirst
                m.startSecond = startSecond
                m.length = length
                addMatchIfNotOverlapping(globalMatchs, m)
    return ComparisonResult(first, second, globalMatchs)

import sys
from antlr4 import *

from tree.Python3Lexer import Python3Lexer

class ComparisonResult:

    def __init__(self, first, second, matchs):
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


def getTokenTypes(file: str):
    input_stream = FileStream(file)
    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)

    result = []

    for i in range(stream.getNumberOfOnChannelTokens() - 1):
        tt = stream.tokens[i].type
        result.append(tt)

    return result
    
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

def comparison(first, second) -> ComparisonResult:
    globalMatchs = []
    for startFirst in range(len(first)):
        for startSecond in range(len(second)):
            length = 0
            while first[startFirst + length] == second[startSecond + length]:
                length += 1
                if startSecond + length >= len(second):
                    break
                if startFirst + length >= len(first):
                    break
            if length > 1:
                m = Match()
                m.startFirst = startFirst
                m.startSecond = startSecond
                m.length = length
                addMatchIfNotOverlapping(globalMatchs, m)
    return ComparisonResult(first, second, globalMatchs)
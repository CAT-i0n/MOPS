
import sys
from antlr4 import *

from tree.Python3Lexer import Python3Lexer



class Match:
    startFirst = 0
    startSecond = 0
    length = 0
    
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
    
def addMatchIfNotOverlapping(matchs, match):
    for m in matchs:
        if m.overlaps(match):
            return
    matchs.append(match)

def comparison(first, second):
    if len(first) > len(second):
        return comparison(second, first)
  
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

    similarity = 0
    for i in range(len(globalMatchs)):
        similarity += globalMatchs[i].length

    similarityFirst = similarity / len(first)
    similaritySecond = similarity / len(second)

    return max(similarityFirst, similaritySecond)

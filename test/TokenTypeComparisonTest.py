import sys
sys.path.append('../')
from alg.TokenTypeComparison import *


if __name__ == "__main__":
    file1 = 'examples/test.py'
    file2 = 'examples/test2.py'
    printComparisonReport(file1, file2)
    
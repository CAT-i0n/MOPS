import sys
sys.path.append('../')

from alg.TokenTypeComparison import *


if __name__ == "__main__":
    test_tokens = getTokenTypes('examples/test.py')
    test2_tokens = getTokenTypes('examples/test2.py')
    c = comparison(test_tokens, test2_tokens).similarity()
    print(c)

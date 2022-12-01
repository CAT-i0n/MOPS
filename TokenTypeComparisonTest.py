
from alg.TokenTypeComparison import *


if __name__ == "__main__":
    test_tokens = getTokenTypes('tree/test.py')
    test2_tokens = getTokenTypes('tree/test2.py')
    c = comparison(test_tokens, test2_tokens)
    print(c)

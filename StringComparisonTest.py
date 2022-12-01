

from alg.StringComparison import *

def getText(file: str):
    with open(file, 'r') as f:
        return f.read()

def mapText(text: str):
    return text

if __name__ == "__main__":
    test_text = getText('tree/test.py')
    test2_text = getText('tree/test2.py')
    test_text = mapText(test_text)
    test2_text = mapText(test2_text)
    c = comparison(test_text, test2_text, 4, 2)
    print(c)


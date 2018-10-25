"""
Convert $ to \\( or \\)

`\( \)` is MathJax default in-line math mode delimiter.
"""

def count_dollar(sentence):
    """
    count $
    """
    count = 0
    for w in sentence:
        if w == '$':
            count += 1
    return count

def replace_dollar(sentence, even=False):
    """
    convert method
    """
    if even:
        return sentence.replace('$', '\\\\)', 1)
    return sentence.replace('$', '\\\\(', 1)


def main():
    s = 'this is example sentence. $a$ is a number. but b is not number. $a + b$ is expression.'
    d = count_dollar(s)
    for i in range(d):
        even = ((i+1) % 2 == 0)
        s = replace_dollar(s, even=even)
    print(s)

if __name__ == '__main__':
    main()

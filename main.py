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

def replace_dollar(sentence):
    """
    convert method
    """
    pass

def main():
    pass

if __name__ == '__main__':
    main()

"""
Convert $ to \\( or \\)

`\( \)` is MathJax default in-line math mode delimiter.
"""

import click

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


def process_line(line):
    """
    行の $ をすべて置換したあらたな文字列を返す
    """
    d = count_dollar(line)
    for i in range(d):
        even = ((i+1) % 2 == 0)
        line = replace_dollar(line, even=even)
    return line

@click.command()
@click.argument('filename')
def process_file(filename):
    with open(filename, 'r') as mdfile:
        lines = mdfile.readlines()
    new_lines = [process_line(line) for line in lines]
    new_sentence = ''.join(new_lines)
    click.echo(new_sentence)

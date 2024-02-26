#!/home/pdajgs/python_labs/py3.7/bin/python3

import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for paragr in doc.paragraphs:
        fullText.append(paragr.text)
    return '\n'.join(fullText)
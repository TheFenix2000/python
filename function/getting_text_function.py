import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for single_aragraph in doc.paragraphs:
        fullText.append(single_aragraph.text)
    return '\n'.join(fullText)
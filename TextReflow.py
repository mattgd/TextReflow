def getText():
    textStr = ""

    # Uses a text file to get text from
    with open('text.txt', 'r') as f:
        for line in f:
            # Remove extraneous newlines except for new paragraphs
            if line == '\n':
                line = line.replace('\n', '\n\n')
            else:
                line = line.replace(' \n', ' ')
                line = line.replace('\n', ' ')
            textStr += line

    return textStr

def reflow(text, chars):
    brokenText = ""
    while len(text) > 0:
        # Add last bit of text to the end
        if (len(text) < chars):
            brokenText += text
            break

        lineStr = text[0:chars]

        # Paragraph breaks
        if '\n\n' in str(lineStr):
            brokenText += lineStr[0:str(lineStr).index('\n\n') + 3]
            text = text[str(text).index('\n\n') + 3:]
            continue

        # Just add the line if it ends in a space or move
        # the word at the end entirely to the next line.
        if lineStr.endswith(' '):
            brokenText += lineStr.strip(' ') + "\n"
            text = text[chars:]
        else:
            lineStr = lineStr.strip(' ')

            if lineStr[-1:] != " " and text[chars:chars + 1] != " ":
                lastSpaceIndex = lineStr.rfind(" ");
                text = text[lastSpaceIndex + 1:].strip()
                brokenText += lineStr[0:lastSpaceIndex] + "\n"
            else:
                brokenText += lineStr + "\n"
                text = text[chars:]

    return brokenText

# Find the longest word in the text
text = getText()
longestWord = 1
while len(text) > 1:
    word = text[0:text.index(' ')]
    if longestWord < len(word):
        longestWord = len(word)
    text = text[text.index(' ') + 1:]

# Get user input for maximum line length
chars = int(input('Enter the maximum number of characters per line: '))

# Enforce longest word as minimum line length
while chars < longestWord:
    print('Maximum number of characters per line must be at least equal to the length of the longest word.')
    chars = int(input('Enter the maximum number of characters per line: '))

# Display the reformatted text
print(reflow(getText(), chars))

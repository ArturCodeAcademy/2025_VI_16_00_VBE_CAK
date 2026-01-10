text = input()
sentences = text.split(". ")
for sentence in sentences:
    print(sentence.count(' '))
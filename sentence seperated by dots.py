sentence=input("enter a sentence:")
words=sentence.split()
first_letters='.'.casefoldjoin(word[0]for word in words)
print(first_letters)

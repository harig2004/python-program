def is_palindrome(s):
    s=s.lower()
    s=''.join(filter(str.isalnum,s))
    return s==s[::-1]
word="a man "
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palinrome")

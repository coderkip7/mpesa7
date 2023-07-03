def is_palindrome(word):
    word = word.replace(" ", "").lower()
    reversed_word = word[::-1]
    return word == reversed_word

input = input("Enter a word or phrase: ")

if is_palindrome(input):
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")

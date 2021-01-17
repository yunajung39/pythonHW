class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')

def palindrome(word):
    if word==word[::-1]:
        print(word)
    else:
        raise NotPalindromeError

try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)



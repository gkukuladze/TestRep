palindromes = lambda lst: list(filter(lambda s: s == s[::-1], lst))

words = ["radar", "hello", "level", "world", "madam", "python"]
palindrome_words = palindromes(words)
print(palindrome_words)

def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    phrase = phrase.capitalize()
    return phrase

#TESTS
print(capitalize('python'))
print(capitalize('only first word'))
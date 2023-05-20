def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    return phrase.title()

#TESTS
print(titleize('this is awesome'), "should be 'This Is Awesome'")
print(titleize('oNLy cAPITALIZe fIRSt'), "should be 'Only Capitalize First'")
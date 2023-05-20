def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    freq = {}
    vowels = 'aeiou'
    phrase = phrase.lower()
    for ltr in phrase:
        if ltr in vowels:
            freq[ltr] = freq.get(ltr, 0) + 1
    
    return freq

#TESTS
print(vowel_count('rithm school'), "should be {'i': 1, 'o': 2}")
print(vowel_count('HOW ARE YOU? i am great!'), "should be {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}")
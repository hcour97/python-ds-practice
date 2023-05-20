def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a
    
        >>> number_compare(1, 1)
        'Numbers are equal'
        
        >>> number_compare(-1, 1)
        'Second is greater'
        
        >>> number_compare(1, -2)
        'First is greater'
    """
    if a > b:
        return "First number is greater"

    elif a < b:
        return "Second number is greater"
    
    else:
        return "Numbers are equal"

#TESTS
print(number_compare(4,5), "Should return second number is greater")
print(number_compare(100,90), "Should return first number is greater")
print(number_compare(40,40), "should return numbers are equal")
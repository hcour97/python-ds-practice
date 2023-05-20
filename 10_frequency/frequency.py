def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    results = {}
    for n in lst:
        results[n] = results.get(n, 0) + 1

    if search_term not in results:
        return 0
    
    return results.get(search_term)

 

#TESTS
print(frequency([1, 4, 3, 4, 4], 4), "should be 3")
print(frequency([1, 4, 3], 7), "should be 0")
print(frequency(["apples", "potatoes", "apples", "oranges", "bananas"], "apples"), "should be 2")
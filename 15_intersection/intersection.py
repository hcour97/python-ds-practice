def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    l1 = set(l1)
    l2 = set(l2)
    return list(l1 & l2)

    ## OR: 
    ## set2 = set(l2)
    ## return [val for val in l1 if val in set2]

#TESTS
print(intersection([1, 2, 3], [2, 3, 4]), "should be [2,3]")
print(intersection([1, 2, 3], [1, 2, 3, 4]), "should be [1,2,3]")
print(intersection([1, 2, 3], [3, 4]), "should be [3]")
print(intersection([1, 2, 3], [4, 5, 6]), "should be []")
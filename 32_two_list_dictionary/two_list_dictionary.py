def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    the_dict = {}

    for idx, val in enumerate(keys):
        the_dict[val] = values[idx] if idx < len(values) else None
    
    return the_dict

#TESTS
print(two_list_dictionary(['x', 'y', 'z'], [9, 8, 7]), "should be {'x': 9, 'y': 8, 'z': 7}")
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]), "should be {'a': 1, 'b': 2, 'c': 3, 'd': None}")
print(two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4]), "should be {'a': 1, 'b': 2, 'c': 3}")
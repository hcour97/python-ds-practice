def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """

    if lst:
        return lst[-1]
    else:
        return(None)

# list = ["apple", "orange", "banana"]
# print(len(list))
# print(list[len(list)-1])

#TESTS
print(last_element([1,2,3]), "should be 3")
print(last_element([]), "should be None")
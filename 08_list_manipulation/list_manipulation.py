def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]
        

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

    if command == "add":
        if location == "beginning":
            lst.insert(0, value)
            return lst
        if location == "end":
            lst.append(value)
            return lst
        
    if command == "remove":
        if location == "end":
            return lst.pop() #list.pop removes the last item
        elif location == "beginning":
            lst.reverse()
            return lst.pop()

    else:
        return None



#TESTS
print(list_manipulation([1, 2, 3], 'remove', 'end'), "should be 3")
print(list_manipulation([1, 2, 3], 'remove', 'beginning'), "should be 1")
print(list_manipulation([1, 2, 3], 'add', 'beginning', 20), "should be [20,1,2,3]")
print(list_manipulation([20,1,2,3], 'add', 'end', 30), "should be [20,1,2,3,30")
print(list_manipulation([1,2,3], 'foo', 'end'), "should return None")
print(list_manipulation([1,2,3], 'add', 'dunno'), "should return None")

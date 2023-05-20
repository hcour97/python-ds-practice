def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    return [val for val in lst if val]

#TEST
print(compact([0, 1, 2, '', [], False, (), None, 'All done']), "should be [1,2,'All done]")
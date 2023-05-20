def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    numbers = {}
    for num in nums:
        numbers[num] = numbers.get(num, 0) + 1
    
    max_value = max (numbers.values())

    for (num,freq) in numbers.items():
        if freq == max_value:
            return num

#TESTS
print(mode([1, 2, 1]), "should be 1")
print(mode([2, 2, 3, 3, 2]), "should be 2")



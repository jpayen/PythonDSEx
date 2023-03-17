def freqCounter(numSet):
    """returns frequency counter for numSet"""
    count = {}
    for i in numSet:
        count[i] = count.get(i , 0) + 1
    return count

def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return freqCounter(str(num1)) == freqCounter(str(num2))
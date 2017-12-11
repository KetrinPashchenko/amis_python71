numbers = [float(i) for i in input().split()]


def secondMaxNumber(numbers):
    """
    Ця функція повертає другий максимальний елемент
    Args:
        numbers: список

    Returns: дійсне числa

    Exampples:
        >>> print(sumSequence([1 2 3 4 5 6 7 8 9]))
        8
        >>> print(sumSequence([1 2 3 4 5 j 7 8 9]))
        File "C:/Users/User/Desktop/Python/12/task1.py",
        line 1, in <listcomp>
        numbers = [float(i) for i in input().split()]
        ValueError: could not convert string to float: 'f'
    """
    numbers.remove(min(numbers))
    if len(numbers) == 2:
        return int(min(numbers))
    else:
        return(secondMaxNumber(numbers))
print(secondMaxNumber(numbers))

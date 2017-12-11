elemеnts = [float(i) for i in input().split()]


def minNumber(elements):


    """
    Ця функція повертає найменший елемент зі списку elemtnts

    Args:
        elemtns: список

    Returns:
        elements: дійсне число

    Exampples:
        >>>print(sumSequence([4, 6, 7, 3, 9, 9, 0, 0))
        0.0

        >>>print(sumSequence([6, 0, 0, f] ))
        Traceback (most recent call last):
        File "C:/Users/User/Desktop/Python/11/task2(11).py",
        line 1, in <listcomp>
        elemеnts = [float(i) for i in input().split()]
        ValueError: could not convert string to float: 'f'

    """
    if len(elements) != 1:
        if elements[0] >= elements[1]:
            return minNumber(elements[1:])
        else:
            del elements[1]
            return minNumber(elements)
    else:
        return elements[0]

print(minNumber(elemеnts))

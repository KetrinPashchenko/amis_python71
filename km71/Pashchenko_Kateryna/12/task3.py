elements = [int(i) for i in input().split()]


def groups(elements, i=0, z=0, k=0):
    """
    Ця функця повертає найбільшу кількість елементів,
    що стоять поряд у списку
    Args:
        elements: список натуральних чисел
        i:  чило
        ter:  чило
        k: число
    Returns:
        натуральне число
    Examples:
        >>> print(1 2 3 4 4 4 5 6 1 1 1 1 3))
        4

    """
    if i < len(elements) - 1 and elements[i] == elements[i + 1]:
        k += 1

        return groups(elements, i + 1, z, k)
    else:
        return k, z


def quantity(elements, i, k):
    if i < len(elements):
        d = groups(elements, i, 0, 1)
        if k < d[0]:
            k = d[0]
        return quantity(elements, i + 1, k)
    else:
        return k
print(quantity(elements, 0, 0))

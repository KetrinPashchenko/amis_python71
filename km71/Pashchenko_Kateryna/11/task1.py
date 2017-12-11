x = float(input())
i = int(input())

while x == "1":
    x = float(input("Число х не коректоне. Спробуйте ще раз:"))
else:
    x = float(x)

def sumSequence(x, i):
    """
    Ця функція обчислює загальну суму послідовності
    ((2 * x + 1) ** i)/(x - 1),
    при введених користувачем змінних i та х
    Args:
        x: дійсне число
        i: ціле число

    Returns дійсне числa

    Exampples:
        >>> print(sumSequence(3,4))
        1400.0

        >>> print(sumSequence(-3,4))
        -130

        >>>print(sumSequence(0.3,7))
        -36.13622857142858

        >>>print(sumSequence(1,5))
        File "C:/Users/User/PycharmProjects/untitled3/task1.py",
        line 37,in sumSequence
        t = ((2 * x + 1) ** i)/(x - 1)
        ZeroDivisionError: float division by zero

        >>>print(sumSequence(1,5))
        Traceback (most recent call last):
        File "C:/Users/User/PycharmProjects/untitled3/task1.py"
        line 48,in <module>
        print(sumSequence(x,i))
    """

    if 1 < i:
        t = ((2 * x + 1) ** i)/(x - 1)
        return (t + sumSequence(x, i-1))
    elif i == 1:
        return((2 * x + 1) ** i)/(x - 1)

def testOnesDigit():
    print("Тест sumSequence()...", end="")
    assert(sumSequence(-3, 4) == -130)
    assert(sumSequence(3, 4) == 1400)
    assert(sumSequence(0.3, 5) == -36.13622857142858)
    print("Все вірно!")

testOnesDigit()
print(sumSequence(x, i))

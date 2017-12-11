list = [i for i in input().split()]

def function(list):
    """
    Ця функція повертає список  в зворотньому порядку

    Args:
        list: список

    Returns:
        list: дійсне число

    Exampples:
        print(1 2 3 4 5 6 7 8 9)
        9 8 7 6 5 4 3 2 1
    """
    l = len(list)
    if (l-1) == 0:
        answer = list[0]
    else:
        answer = str(list[l-1]) +' '+ function(list[:(l-1)])
    return answer
print(function(list))

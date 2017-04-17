#!/usr/bin/dev python


def fact(n):
    '''

    >>> fact(5)
    120

    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print("i am 1")

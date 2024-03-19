import doctest


# ---------------------------------------------------------------------
# Approach 1: Functions within Functions                            ***
# ---------------------------------------------------------------------
def solution(s: str) -> str:
    """Write a function, it should return a new function that always
    returns 'Hello World'. A string could be passed to the function but
    it should still always return 'Hello World'.

    Examples:
        >>> solution('hi')
        'Hello World'
        >>> solution('how are you?')
        'Hello World'
        >>> solution('what is your name?')
        'Hello World'
    """
    def return_hello_world(t: str) -> str:
        return 'Hello World'

    return return_hello_world(s)


if __name__ == '__main__':
    doctest.testmod()

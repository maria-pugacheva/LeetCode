import doctest
from typing import List


def solution(tokens: List[str]) -> int:
    """Given an array of strings tokens that represents an arithmetic
    expression in Reverse Polish Notation (RPN), evaluate the expression
    and return an integer representing its value.

    Preconditions:
        - tokens[i] is either an operator: "+", "-", "*", or "/", or an
        integer in the range [-200, 200]
        - Division truncates toward zero, and there will be no
        division by zero

    Examples:
        >>> solution(["2","1","+","3","*"])
        9
        >>> solution(["4","13","5","/","+"])
        6
        >>> solution(["4","-2","/","2","-3","-","-"])
        -7
        >>> solution(["10","6","9","3","+","-11","*","/","*","17","+"])
        17
    """
    stack = []
    for ch in tokens:
        if ch == '+':
            stack.append(stack.pop() + stack.pop())
        elif ch == '-':
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
        elif ch == '*':
            stack.append(stack.pop() * stack.pop())
        elif ch == '/':
            b = stack.pop()
            a = stack.pop()
            stack.append(int(a / b))
        else:
            stack.append(int(ch))
    return stack[-1]


if __name__ == '__main__':
    doctest.testmod()


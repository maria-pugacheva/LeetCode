import doctest


# ---------------------------------------------------------------------
# Approach 1: Stack. Time: O(n). Space: O(2n)                       !**
# ---------------------------------------------------------------------
def solution_one(path: str) -> str:
    """Given an absolute path for a Unix-style file system, which begins
    with a slash '/', transform this path into its simplified canonical
    path.

    Examples:
        >>> solution_one('/home/')
        '/home'
        >>> solution_one('/home//foo/')
        '/home/foo'
        >>> solution_one('/home/user/Documents/../Pictures')
        '/home/user/Pictures'
        >>> solution_one('/../')
        '/'
        >>> solution_one('/.../a/../b/c/../d/./')
        '/.../b/d'
        >>> solution_one('/..hidden')
        '/..hidden'
        >>> solution_one('/hello../world')
        '/hello../world'
        >>> solution_one('/../..ga/b/.f..d/..../e.hello./.a')
        '/..ga/b/.f..d/..../e.hello./.a'
    """
    stack = []
    for part in path.split('/'):
        if part == '.' or not part:
            continue
        elif part == '..':
            if stack:
                stack.pop()
        else:
            stack.append(part)
    return '/' + '/'.join(stack)


if __name__ == '__main__':
    doctest.testmod()

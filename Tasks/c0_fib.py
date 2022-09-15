def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    print(n)
    return 0


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    print(n)
    return 0


def generator_fib(n):
    if n < 0:
        raise ValueError

    a = 0
    yield a

    b = 1
    yield b

    for _ in range(1, n):
        a, b = b, a+b
        yield b


N = 10

list_fin_iterative = [fib_iterative(i) for i in range(N)]
list_generator = [num for num in generator_fib(N-1)]

import ipdb


def main() -> None:
    """Execute the main function."""
    print("Hello, World!")
    result = fibonacci(5)
    print(result)
    print("Goodbye, World!")


def fibonacci(n: int) -> int:
    """Fibonacci function.

    Args:
    ----
        n (int): number.

    Returns:
    -------
        int: result number.

    """
    breakpoint()
    # ipdb.set_trace()
    if n == 1:
        return 0
    if n == 2:  # noqa: PLR2004
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    main()

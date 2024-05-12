import objgraph


def main() -> None:
    """Execute the main function."""
    computate_something()
    # objgraph.show_growth(limit=3)
    objgraph.show_growth()  # doctest: +RANDOM_OUTPUT


class MyBigFatObject:  # noqa: D101
    pass


def computate_something(_cache=None) -> None:  # noqa: ANN001
    """Execute the main function."""
    if _cache is None:
        _cache = [None] * 43
    _cache[42] = {"foo": MyBigFatObject(), "bar": MyBigFatObject()}
    x = MyBigFatObject()
    print("computate_something")
    print(x)


if __name__ == "__main__":
    main()

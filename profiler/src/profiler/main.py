import cProfile
import re

import objgraph


def objgraph_function() -> None:
    """Execute the main function."""
    computate_something()
    objgraph.show_growth(limit=3)
    print("")
    print("--------------------------------")
    print("")


def profiler_function() -> None:
    """Execute the main function."""
    print("profiler_function")
    # pattern = re.compile("foo|bar")  # noqa: ERA001
    # print(f"Compiled Regex (foo|bar): {pattern}")  # noqa: ERA001
    # cProfile.runctx("pattern", globals(), locals()) # noqa: ERA001
    cProfile.run('re.compile("foo|bar")')


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
    objgraph_function()
    profiler_function()

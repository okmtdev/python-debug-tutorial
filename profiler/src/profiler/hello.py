import time


def main() -> None:  # noqa: D103
    word = "Hello world!"
    for s in word:
        time.sleep(1)
        print(s)


if __name__ == "__main__":
    main()

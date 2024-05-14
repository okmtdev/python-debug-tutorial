from line_profiler import profile


@profile
def is_prime(n):
    """
    Check if the number "n" is prime, with n > 1.

    Returns a boolean, True if n is prime.
    """
    max_val = n**0.5  # n の平方根を計算
    stop = int(max_val + 1)  # 探索する最大値を整数に丸める
    for i in range(2, stop):  # 2からstopまでの数でnを割ります
        if n % i == 0:  # もしnがiで割り切れたら、nは素数ではない
            return False
    return True


@profile
def find_primes(size):
    """
    0から指定されたsizeまでの範囲で素数を探し、リストとして返します。

    素数のリストを返します。
    """
    primes = []
    for n in range(size):
        flag = is_prime(n)
        if flag:
            primes.append(n)
    return primes


@profile
def main():
    print("start calculating")
    primes = find_primes(100000)
    print(f"done calculating. Found {len(primes)} primes.")


if __name__ == "__main__":
    main()

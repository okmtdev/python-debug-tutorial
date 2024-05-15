# line_profiler

line_profiler -- a module for doing line-by-line profiling of functions. kernprof is a convenient script for running either line_profiler or the Python standard library’s cProfile or profile modules, depending on what is available.

https://github.com/pyutils/line_profiler

```
$ rye run add line-profiler
```

プロファイルしたい関数に `@profile` をつけると自動的に解析してくれるる。

`LINE_PROFILE` 環境変数に 1 を指定することでプロファイル機能が有効化される

```
$ LINE_PROFILE=1 rye run python src/lm_profiler/line_main.py
start calculating
done calculating. Found 9594 primes.
Timer unit: 1e-09 s

  0.48 seconds - /Users/okmt/plays/python/python-debug-tutorial/lm_profiler/src/lm_profiler/line_main.py:4 - is_prime
  1.05 seconds - /Users/okmt/plays/python/python-debug-tutorial/lm_profiler/src/lm_profiler/line_main.py:19 - find_primes
  1.09 seconds - /Users/okmt/plays/python/python-debug-tutorial/lm_profiler/src/lm_profiler/line_main.py:34 - main
Wrote profile results to profile_output.txt
Wrote profile results to profile_output_2024-05-14T171516.txt
Wrote profile results to profile_output.lprof
To view details run:
python -m line_profiler -rtmz profile_output.lprof
```

これの結果を見るには lprof ファイルを指定します。

```
$ python -m line_profiler -rtmz profile_output.lprof

Timer unit: 1e-06 s

Total time: 0.483702 s
File: /Users/okmt/plays/python/python-debug-tutorial/lm_profiler/src/lm_profiler/line_main.py
Function: is_prime at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @profile
     5                                           def is_prime(n):
     6                                               """
     7                                               Check if the number "n" is prime, with n > 1.
     8
     9                                               Returns a boolean, True if n is prime.
    10                                               """
    11    100000      10021.0      0.1      2.1      max_val = n**0.5  # n の平方根を計算
    12    100000      13785.0      0.1      2.8      stop = int(max_val + 1)  # 探索する最大値を整数に丸める
    13   2755287     208347.0      0.1     43.1      for i in range(2, stop):  # 2からstopまでの数でnを割ります
    14   2745693     242532.0      0.1     50.1          if n % i == 0:  # もしnがiで割り切れたら、nは素数ではない
    15     90406       8148.0      0.1      1.7              return False
    16      9594        869.0      0.1      0.2      return True

Total time: 1.05496 s
File: /Users/okmt/plays/python/python-debug-tutorial/lm_profiler/src/lm_profiler/line_main.py
Function: find_primes at line 19

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    19                                           @profile
    20                                           def find_primes(size):
    21                                               """
    22                                               0から指定されたsizeまでの範囲で素数を探し、リストとして返します。
    23
    24                                               素数のリストを返します。
    25                                               """
    26         1          0.0      0.0      0.0      primes = []
    27    100001       9657.0      0.1      0.9      for n in range(size):
    28    100000    1035901.0     10.4     98.2          flag = is_prime(n)
    29    100000       7872.0      0.1      0.7          if flag:
    30      9594       1531.0      0.2      0.1              primes.append(n)
    31         1          0.0      0.0      0.0      return primes

Total time: 1.08748 s
File: /Users/okmt/plays/python/python-debug-tutorial/lm_profiler/src/lm_profiler/line_main.py
Function: main at line 34

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    34                                           @profile
    35                                           def main():
    36         1         12.0     12.0      0.0      print("start calculating")
    37         1    1087448.0    1e+06    100.0      primes = find_primes(100000)
    38         1         24.0     24.0      0.0      print(f"done calculating. Found {len(primes)} primes.")

  0.48 seconds - /Users/okmt/plays/python/python-debug-tutorial/lm_profiler/src/lm_profiler/line_main.py:4 - is_prime
  1.05 seconds - /Users/okmt/plays/python/python-debug-tutorial/lm_profiler/src/lm_profiler/line_main.py:19 - find_primes
  1.09 seconds - /Users/okmt/plays/python/python-debug-tutorial/lm_profiler/src/lm_profiler/line_main.py:34 - main
```

For more control over the outputs, run your script using kernprof. The following invocation will run your script, dump results to demo_primes.py.lprof, and display results.

```
$ LINE_PROFILE=1 rye run python -m kernprof -lvr src/lm_profiler/line_main.py
start calculating
done calculating. Found 9594 primes.
Wrote profile results to line_main.py.lprof
Timer unit: 1e-06 s

Total time: 0.55552 s
File: src/lm_profiler/line_main.py
Function: is_prime at line 4

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
     4                                           @profile
     5                                           def is_prime(n):
     6                                               """
     7                                               Check if the number "n" is prime, with n > 1.
     8
     9                                               Returns a boolean, True if n is prime.
    10                                               """
    11    100000       9996.0      0.1      1.8      max_val = n**0.5  # n の平方根を計算
    12    100000      14379.0      0.1      2.6      stop = int(max_val + 1)  # 探索する最大値を整数に丸める
    13   2755287     248082.0      0.1     44.7      for i in range(2, stop):  # 2からstopまでの数でnを割ります
    14   2745693     273393.0      0.1     49.2          if n % i == 0:  # もしnがiで割り切れたら、nは素数ではない
    15     90406       8762.0      0.1      1.6              return False
    16      9594        908.0      0.1      0.2      return True

Total time: 1.15038 s
File: src/lm_profiler/line_main.py
Function: find_primes at line 19

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    19                                           @profile
    20                                           def find_primes(size):
    21                                               """
    22                                               0から指定されたsizeまでの範囲で素数を探し、リストとして返します。
    23
    24                                               素数のリストを返します。
    25                                               """
    26         1          0.0      0.0      0.0      primes = []
    27    100001      10620.0      0.1      0.9      for n in range(size):
    28    100000    1130731.0     11.3     98.3          flag = is_prime(n)
    29    100000       7711.0      0.1      0.7          if flag:
    30      9594       1314.0      0.1      0.1              primes.append(n)
    31         1          0.0      0.0      0.0      return primes

Total time: 1.18313 s
File: src/lm_profiler/line_main.py
Function: main at line 34

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    34                                           @profile
    35                                           def main():
    36         1         10.0     10.0      0.0      print("start calculating")
    37         1    1183107.0    1e+06    100.0      primes = find_primes(100000)
    38         1         17.0     17.0      0.0      print(f"done calculating. Found {len(primes)} primes.")
```

- Note: the -r flag will use “rich-output” if you have the rich module installed.

# memory_profiler

memory_profiler -- This is a python module for monitoring memory consumption of a process as well as line-by-line analysis of memory consumption for python programs. It is a pure python module which depends on the psutil module.

Note: This package is no longer actively maintained. I won’t be actively responding to issues. If you’d like to volunteer to maintain it, please drop me a line at f@bianp.net

# psutil

psutil -- psutil (process and system utilities) is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python. It is useful mainly for system monitoring, profiling and limiting process resources and management of running processes. It implements many functionalities offered by classic UNIX command line tools such as ps, top, iotop, lsof, netstat, ifconfig, free and others.

cpu

```
# CPU 利用率
psutil.cpu_percent(interval=1)

# ~
psutil.cpu_count()

# ~
psutil.cpu_stats()

# ~
psutil.cpu_freq()

# ~
psutil.getloadavg()
```

memory

```
# ~
psutil.virtual_memory()

# ~
psutil.swap_memory()
```

disks

```
# ~
psutil.disk_partitions()

# ~
psutil.disk_usage('/')

# ~
psutil.disk_io_counters(perdisk=False)
```

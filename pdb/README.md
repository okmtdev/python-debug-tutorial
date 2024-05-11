# pdb

pdb -- Python 標準実装のデバッガ

https://docs.python.org/ja/3/library/pdb.html

Python プログラム用の対話型ソースコードデバッガ。事後解析デバッギングもサポートし、プログラムの制御下で呼び出すことができる

```
import pdb; pdb.set_trace()
# or
breakpoint() # Python 3.7以降はビルトイン関数breakpoint()がset_trace()の代わりに使えるように
```

Python 実行時に引数を指定して起動することもできる

```
$ rye run python -m pdb src/rdb/main.py
```

| command                  | short command | description                                                                                 |
| ------------------------ | ------------- | ------------------------------------------------------------------------------------------- |
| help                     | h             | 利用できるコマンドの一覧を表示                                                              |
| where                    | w             | スタックの底にある最も新しいフレームと一緒にスタックトレースを表示                          |
| down                     | d             | スタックフレーム内で現在のフレームを count レベル (デフォルトは 1) 新しいフレーム方向に移動 |
| up                       | u             | スタックフレーム内で現在のフレームを count レベル (デフォルトは 1) 古いフレーム方向に移動   |
| break (lineno, function) | b             | 現在のファイルのその行番号の場所にブレークポイントを設定                                    |
| list                     | l             | 現在のファイルのソースコードを表示                                                          |
| return                   | r             | 関数の終わりまで実行する                                                                    |
| quit                     | q             | デバッグを終了する                                                                          |

# ipdb

pdb モジュールと同じインターフェイスでより良いシンタックスハイライトでデバッグ可能

使い方は pdb とほぼ同じ

![ipdb](./images/ipdb.png)

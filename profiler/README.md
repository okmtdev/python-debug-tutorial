# profiler

Describe your project here.

# objgraph

objgraph -- module that lets you visually explore Python object graphs.

https://github.com/mgedmin/objgraph

You’ll need graphviz if you want to draw the pretty graphs.

`graphviz`で綺麗にグラフをかけ、`xdot`でインタラクティブに仕様が可能なそう

[Python Object Graphs manual](https://objgraph.readthedocs.io/en/stable/)

quick start

```
>>> import objgraph
>>> x = []; y = [x, [x], dict(x=x)]
>>> objgraph.show_refs([y], filename='./out/sample-graph.png')
>>> Graph written to /var/folders/cn/4k0q58ws55q_vr20lpgvrkjw0000gn/T/objgraph-ka3r4xft.dot (4 nodes)
>>> Image generated as ./out/sample-graph.png
```

backreferences

```
>>> objgraph.show_backrefs([x], filename='./out/sample-backref-graph.png')
Graph written to /var/folders/cn/4k0q58ws55q_vr20lpgvrkjw0000gn/T/objgraph-oft8o4t4.dot (7 nodes)
Image generated as ./out/sample-backref-graph.png
```

memory leak example

`objgraph`は元々 memory leak を発見する目的で開発された

[`show_most_common_types`](https://objgraph.readthedocs.io/en/stable/objgraph.html#objgraph.show_most_common_types)でメモリ上のオブジェクトの概要を素早く見ることができる

```
>>> objgraph.show_most_common_types()
function                   2063
wrapper_descriptor         1138
dict                       974
tuple                      886
builtin_function_or_method 790
method_descriptor          762
ReferenceType              716
getset_descriptor          392
type                       318
member_descriptor          311
```

leak の探し方

```
>>> class MyBigFatObject(object):
...     pass
...
>>> def computate_something(_cache={}):
...     _cache[42] = dict(foo=MyBigFatObject(),
...                       bar=MyBigFatObject())
...     # a very explicit and easy-to-find "leak" but oh well
...     x = MyBigFatObject() # this one doesn't leak
```

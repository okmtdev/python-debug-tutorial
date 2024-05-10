Python プロジェクトを初期化することが増えたので、Python プロジェクトの手順書をば

「Flake8 + Black + isort はもうすべて Ruff だけで置き換えられる」とのことなので、Ruff に統一します。

vscode の設定

```
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnType": true,
    // ...
  }
```

```
// formatter
ruff format .

// linter
ruff check . --fix
```

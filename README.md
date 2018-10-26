# dollar-convert-inline-math

普段 `$...$` と数式を書いているがデフォルトのMathJaxに合わせて`\(\)`とインライン数式のデリミタを変更できるようにした。

このコマンドを作成することにより得られる作者の実益よりも下記の2つのライブラリを試すことが主目的でこのプロジェクトは作成された。

* [pypa/pipenv: Python Development Workflow for Humans\.](https://github.com/pypa/pipenv)
* [pallets/click: Python composable command line interface toolkit](https://github.com/pallets/click)

# Example

```
$ cat foo.md
# foo

$a = b$, $a+b$, $\sin x + b$
$ do2im foo.md  # 出力ファイルを指定しない場合は標準出力される
# foo

\\(a = b\\), \\(a+b\\), \\(\sin x + b\\)
$ do2im foo.md -o output.md  # -o オプションでファイル出力
$ cat output.md
# foo

\\(a = b\\), \\(a+b\\), \\(\sin x + b\\)
```
# LICENSE

MIT

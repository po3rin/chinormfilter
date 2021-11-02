# chinormfilter

[![PyPi version](https://img.shields.io/pypi/v/chinormfilter.svg)](https://pypi.python.org/pypi/chinormfilter/)
![PyTest](https://github.com/po3rin/chinormfilter/workflows/PyTest/badge.svg)
[![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-390/)
![](https://img.shields.io/pypi/l/chinormfilter)

Filter synonym written in lucene format to avoid duplication with Sudachi normalization. Mainly used when migrating to sudachi analyzer.

## Usage

```sh
$ chinormfilter tests/test.txt -o out.txt
```

filtered result is following.

```txt
レナリドミド,レナリドマイド
リンゴ => 林檎
飲む,呑む
tlc => tlc,全肺気量
リンたんぱく質,リン蛋白質,リンタンパク質

↓ filter

レナリドミド,レナリドマイド
tlc => tlc,全肺気量
```

### Specify system dict

```sh
$ chinormfilter tests/test.txt -s full -o out.txt
```

### Use Custom Dict

Specify dict via sudachi.json

```sh
$ chinormfilter tests/test.txt -s sudachi.json -o out.txt
```

## TODO
- [ ] custom dict test

# tui-pointer

A terminal visualization library for two-pointer algorithm problems, built with [Rich](https://github.com/Textualize/rich).

[![asciicast](https://asciinema.org/a/kpBVEpBORZM9Emff.svg)](https://asciinema.org/a/kpBVEpBORZM9Emff)

## Requirements

- Python 3.10+

## Setup & Running

Install dependencies and run all examples:

```sh
make install
make run
```

Or run individual examples:

```sh
make run-two-sum             # two-sum search
make run-remove-duplicates   # remove duplicates in-place
make run-remove-element      # remove element in-place
```

## Manual Setup (without make)

```sh
python3 -m venv .venv
.venv/bin/pip install -e .
.venv/bin/python3 examples/example.py
```

## Examples

| Example | Algorithm | Input | Result |
|---------|-----------|-------|--------|
| `example.py` | Two-sum search | `[1, 3, 5, 7, 9, 11]`, target=10 | indices `(0, 4)` → `1 + 9 = 10` |
| `example_remove_duplicates.py` | Remove duplicates in-place | `[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]` | `k=5`, result `[0, 1, 2, 3, 4]` |
| `example_remove_element.py` | Remove element in-place | `[3, 2, 2, 3, 4, 3, 5]`, val=3 | `k=4`, result `[5, 2, 2, 4]` |

## Cleanup

```sh
make clean
```

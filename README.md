# rdx

A radix conversion module.

## Installation

```
pip install rdx
```

## Usage

This module provides the following functions:
- `int_to_digits(n, b=10)` to convert a number into a digit representation,
- `digits_to_int(d, b=10)` to retrieve a number from a digit representation and
- `int_to_len_digits(n, b=10)` to calculate how many digits will be needed.
```python
>>> from rdx import *
>>> int_to_digits(42, 2)
[0, 1, 0, 1, 0, 1]
>>> int_to_digits(42, 16)
[10, 2]
>>> digits_to_int([27, 1], 42)
69
>>> int_to_len_digits(1024, 2)
11
```
As a digit representation a list with integers is used, where every element
represents a digit, all ordered in ascending positions.

## License (MIT)

Copyright (c) 2023 Sebastian Gössl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

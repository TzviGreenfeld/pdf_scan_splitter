# Scan splitter

Re-organize a pdf file of an horizontally scanned book

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Support](#support)

## Installation

Download scan_splitter.py and install libraries from requirements.txt


```
$ git clone https://github.com/TzviGreenfeld/pdf_scan_splitter
$ pip install -r requirements.txt
```

## Usage

Send as first argument the file name, second argument is the output file name (both should be *.pdf)
second and third arguments rightmost x value (in px) of left page and the leftmost x value of the right pages (they can overlap)
By default, it will split in the middle.

```
$ python3 scan_splitter.py <in.pdf> <out.pdf> <x1> <x2>
```


## Support

Please [open an issue](https://github.com/TzviGreenfeld/pdf_scan_splitter/issues/new) for support.

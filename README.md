pquery
======

grep for HTML; CLI for pyquery

## Demo

```
$curl -s https://github.com/hupili/pquery | pquery '.content a' -p text
.gitignore
LICENSE
MANIFEST.in
README.md
pquery
setup.py
```

`pquery` is intended to integrate into your UNIX pipeline.

## Install

`pip install pquery`

## Syntax

```
Usage:
    pquery <selector>
    pquery <selector> -p <projector>
    pquery <selector> -f <format_string>
    pquery -h | --help

Options:
    -p: project the dict onto field `<projector>`.
    -f: equivalent of `<format_string>.format(item)`,
        where item is the dict form of one selected HTML element.
    -h | -v: shows this doc.

Dict keys:
    'tag': The HTML tag
    'html': Inner HTML of the element
    'text': Inner text of the element
    ...: [optional] Other attributes: e.g. 'href'
```

## Why

`grep` is powerful for **lines**.
HTML is structured and not line processor friendly.
CSS selector is a natural grep for HTML.
This script simply wraps [pyquery](http://pyquery.readthedocs.org/en/latest/) to provide a CLI.

## Example 1

A [course webpage](https://class.coursera.org/crypto-008/wiki/LectureSlidesPublicCourse)
lists slides in `pdf` and `pptx`.
Want to download all the PDFs.
This saves you some click.

```
wget --load-cookies=cookies.txt -O- 'https://class.coursera.org/crypto-008/wiki/LectureSlidesPublicCourse' | pquery a -p href | grep pdf | xargs -P 5 -I{} wget {}
```

It's tedious to directly grep the PDF links out from HTML.


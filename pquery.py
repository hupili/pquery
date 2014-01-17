'''
grep for HTML; CLI for pyquery

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
'''

import sys
import docopt
from pyquery import PyQuery as pq

# The workflow is driven by iterator/generator

def array_output(a):
    for i in a:
        if i:
            sys.stdout.write(str(i) + '\n')

def project(a, projector):
    # For initial version, only support grepping one field.
    # Support multiple fields if there are good use cases.
    #fields = set(projector.split(','))
    for i in a:
        yield i.get(projector, None)

def format_dict(a, format_string):
    for i in a:
        yield format_string.format(**i)

def html_element_to_dict(a):
    for i in a:
        d = {}
        try:
            d['html'] = i.html()
        except Exception as e:
            # log the exception in verbose mode?
            # Possible exceptions:
            #    * some utf-8 errors
            d['html'] = None
        h = i[0]
        d['tag'] = h.tag
        d['text'] = h.text
        d.update(h.attrib)
        yield d

if __name__ == '__main__':
    args = docopt.docopt(__doc__, version='0.1')
    html = sys.stdin.read()
    d = pq(html)
    matches = d(args['<selector>'])
    data = html_element_to_dict(matches.items())
    if args['<projector>']:
        data = project(data, args['<projector>'])
    if args['<format_string>']:
        data = format_dict(data, args['<format_string>'])
    array_output(data)


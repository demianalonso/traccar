#!/usr/bin/python

import re
import os

path = '../web/l10n/'

files = [f for f in os.listdir(path) if os.path.isfile(path + f) and f.endswith('.js') and not f.endswith('en.js')]
for f in files:
    f = path + f

    dict = {}

    for line in open(f).read().splitlines():
        match = re.search("    (\\w+): '(.+)'(,)?", line)
        if match:
            dict[match.group(1)] = match.group(2)

    out = open(f, 'w')

    for line in open(path + 'en.js').read().splitlines():
        match = re.search("    (\\w+): '(.+)'(,)?", line)
        if match:
            if dict.has_key(match.group(1)):
                value = dict[match.group(1)]
            else:
                value = match.group(2) + ' (*)'

            out.write('    ' + match.group(1) + ": '" + value + "'")
            if match.group(3) is not None:
                out.write(',')
            out.write('\n')
        else:
            out.write(line + '\n')

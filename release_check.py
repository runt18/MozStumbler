#!/usr/bin/env python

import sys

props = {}
for line in open('android/properties/private-{0!s}.properties'.format(sys.argv[-1])):
    if len(line.strip()) == 0:
        continue
    if line[0] == '#':
        continue
    k, v = line.strip().split('=')
    props[k] = v
assert 'MapAPIKey' in props, 'MapAPIKey is ok'
assert 'MozAPIKey' in props, 'MozAPIKey is ok'

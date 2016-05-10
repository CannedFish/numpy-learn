#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from StringIO import StringIO

data = '1, 2, 3\n4, 5, 6'
print np.genfromtxt(StringIO(data), delimiter=',')

data = '  1  2  3\n  4  5 67\n890123  4'
print np.genfromtxt(StringIO(data), delimiter=3)

data = '123456789\n  4  7 9\n   4567 9'
print np.genfromtxt(StringIO(data), delimiter=(4, 3, 2))

data = '1 2 3\n4 5 6'
print np.genfromtxt(StringIO(data), usecols=(0, -1))
print np.genfromtxt(StringIO(data), names='a, b, c', usecols=('a, c'))
print np.genfromtxt(StringIO(data), dtype=[(_, int) for _ in 'abc'])

convertfunc = lambda x: float(x.strip('%')) / 100
data = '1, 2.3%, 45\n6, 78.9%, 0'
print np.genfromtxt(StringIO(data), delimiter=','\
    , names=('i', 'p', 'n'), converters={'p': convertfunc})

data = 'N/A, 2, 3\n4, ,???'
kwargs = dict(delimiter=','
    , dtype=int
    , names='a, b, c'
    , missing_values={0:'N/A', 'b': ' ', 2:'???'}
    , filling_values={0:0, 'b':0, 2:-999})
print np.genfromtxt(StringIO(data), **kwargs)


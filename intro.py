#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

x = np.float32(1.0)
y = np.int_([1, 2, 4])
z = np.arange(3, dtype=np.uint8)
print "x=%f, y=%s, z=%s" % (x, y, z)

a = np.array([1, 2, 3], dtype='f')
print a

x1 = np.array([2, 3, 1, 0])
y1 = np.array([[1, 2, 0], [0, 0], [1+1j, 3.]])
z1 = np.array([[1.+0.j, 2.+0.j], [0.+0.j, 0.+0.j], [1.+1.j, 3.+0.j]])
print x1, y1, z1

print np.zeros((2, 3))
print np.linspace(1., 4., 8)
print np.indices((3, 3))


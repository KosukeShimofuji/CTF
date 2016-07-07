#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

p = [70, 152, 195, 284, 475, 612, 791, 896, 810, 850, 737, 1332, 1469, 1120, 1470, 832, 1785, 2196, 1520, 1480, 1449]

i = 0;
for elem in p:
    sys.stdout.write(chr(elem / (i + 1)))
    i += 1


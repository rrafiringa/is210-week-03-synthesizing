#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

TXT = inquisition.SPANISH
SPANISH = 'Spanish'
IDX = inquisition.SPANISH.index(SPANISH)
OFFSET = len(SPANISH[:-3])
print IDX
print OFFSET
FLEMISH = TXT[0:IDX] + 'Flem' + TXT[IDX + OFFSET:]
print FLEMISH

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  Copyright (c) 2018 - EMBL
#
#  File author(s): Dénes Türei (turei.denes@gmail.com)
#
#  This code is not for public use.
#  Please do not redistribute.
#  For permission please contact me.
#
#  Website: http://www.ebi.ac.uk/~denes
#

import imp

import ltp
from ltp import main
from ltp import table

imp.reload(table)
imp.reload(main)
imp.reload(ltp)

r = ltp.ResultsReprocessor(
    source_dir = '/home/denes/documents/ltp/processed_invivo',
    mgfdir = '/home/denes/archive/ltp/mgf_invivo',
    screen = 'invivo',
)

#r.proteins = {'STARD10'}
r.main()

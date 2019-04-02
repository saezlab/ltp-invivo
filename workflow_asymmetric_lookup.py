#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#  Copyright (c) 2019 - EMBL
#
#  File author(s): Dénes Türei (turei.denes@gmail.com)
#
#  This code is not for public use.
#  Please do not redistribute.
#  For permission please contact me.
#
#  Website: http://denes.omnipathdb.org/
#

import imp

import ltp
from ltp import table
from ltp import settings

def reload():
    
    (
        imp.reload(settings),
        imp.reload(table),
        imp.reload(ltp),
    )


infile = settings.get('invivo_all_results_new')

r = table.AsymmetricLookupReprocessor(
    infile = infile,
    ppm_lower = -100,
    ppm_upper = 10,
    da_lower  = -0.07,
    da_upper  = 0.01,
)

#r.proteins = {'STARD10'}
r.main()

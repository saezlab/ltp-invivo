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
#  Website: http://www.ebi.ac.uk/~denes
#

import imp
import os

import ltp
from ltp import main
from ltp import table
from ltp import results

imp.reload(table)
imp.reload(results)
imp.reload(main)
imp.reload(ltp)


r = ltp.ResultsReprocessor(
    source_dir = '/home/denes/documents/ltp/processed_invivo',
    mgfdir = '/home/denes/archive/ltp/mgf_invivo',
    screen = 'invivo',
)

r.rreader.export_df(
    r.df,
    os.path.join('data', 'invivo_postproc_input.tsv')
)

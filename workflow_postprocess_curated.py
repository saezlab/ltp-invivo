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

from lipyd import lipproc
from lipyd import name
from ltp import results
from ltp import ltproteins


def reload():
    
    imp.reload(lipproc)
    imp.reload(name)
    imp.reload(ltproteins)
    imp.reload(results)


rr = results.ResultsReader(
    screen = 'invivo',
    new_layout = True,
)
rr.main()
rr.export()

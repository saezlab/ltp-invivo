# Workflows for the LTP in vivo LC MS/MS screen

The code for the analysis of the screen is distributed into the
following repositories:

* Generic module for MS data processing and lipid identification:
https://git.embl.de/grp-gavin/lipyd
* LTP specific Python module built on top of `lipyd`, with classes for
reading the already manually processed results, reprocessing custom parts,
editing the xlsx tables: https://git.embl.de/grp-gavin/ltp_ms
* Reprocessing workflows on the in vivo data and generating the
post-processing input table (this is the input for in silico validation
and figures); requires `lipyd` and `ltp` modules:
https://git.embl.de/grp-gavin/ltp_invivo
* R code for figures (works from the post-processing input tables):
https://git.embl.de/grp-gavin/ltp_figures

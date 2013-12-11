#!/usr/bin/python

import csv

# read comma-delimited file
with open('myfile.csv','rb') as fin:
    cr = csv.reader(fin, delimiter=',')
    filecontents = [line for line in cr]

# write tab-delimited file
with open('myfile.tsv','wb') as fout:
    cw = csv.writer(fout, quotechar='"', quoting=csv.QUOTE_NONE, delimiter='\t')
    cw.writerows(filecontents)

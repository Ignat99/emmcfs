#!/usr/bin/env python

import MySQLdb
import os

DEBUG = 1
FILES = ["pmccabe.txt"]
#f 
#REG = '%linux%'

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="",
                  db="emmcfs")
x = conn.cursor()


# Get the Data
for file1 in FILES:
    f = open(file1,"r")
    for line in f:
        if DEBUG : print line
        s = line.split()
        if DEBUG : print s
        n = len(s)
        name_full = s[6] + '()'
        x.execute (" UPDATE element SET pmccabe = %s, pmccabe_sum = %s  WHERE  name=%s ", ( s[0], s[2], name_full))
        if DEBUG : print "Number of rows updated: %d" % x.rowcount


conn.close()

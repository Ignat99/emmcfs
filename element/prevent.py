#!/usr/bin/env python

import MySQLdb
import os

DEBUG = 1
FILES = ["cov-query.csv"]
#f 
#REG = '%linux%'

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="",
                  db="emmcfs")
x = conn.cursor()
x.execute (" UPDATE element SET prevent = '', prevent_description = '' ")


# Get the Data
for file1 in FILES:
    f = open(file1,"r")
    for line in f:
        if DEBUG : print line
        s = line.split(',')
        if DEBUG : print s
        n = len(s)
        name_full = s[6] + '()'
        x.execute("SELECT prevent_description FROM element WHERE name = %s", name_full)
        row = x.fetchall()
        old_row = ''
        if (row) :
            for str1 in row:
                old_row = old_row + str1[0]

            description_full = old_row + s[8] + ' : ' + s[9]
        else :
            description_full =  s[8] + ' : ' + s[9]
            
        x.execute (" UPDATE element SET prevent = %s, prevent_description = %s  WHERE  name=%s ", ( s[1], description_full, name_full))
        if DEBUG : print "Number of rows updated: %d" % x.rowcount


conn.close()

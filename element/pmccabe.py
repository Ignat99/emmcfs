#!/usr/bin/env python

import MySQLdb
import os

DEBUG = 1
FILES = ["pmccabe.txt",'']
#REG = '%linux%'

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="",
                  db="emmcfs")
x = conn.cursor()


# Get the Data
for file in FILES:
    infile = open(file,"r")
    while infile:
        line = infile.readline()
#        if DEBUG : print line
        s = line.split()
        if DEBUG : print s
        n = len(s)

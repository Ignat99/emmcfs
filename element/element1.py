#Server Connection to MySQL:

import MySQLdb
import os

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="",
                  db="emmcfs")
x = conn.cursor()

# Let's get the average and our grades:
TP = {"D:":0,"F:":0,"S:":0,"s:":0,"G:":0,"g:":0}
TP1 = {"P:":0,"L:":0}
HWAVE = 0
TOTAL = 0
FILES = ["Code.map"]

SUM1 = 0
DEBUG = 0

PATH = ''
FLAG_PATH = 0

D_ID = ''
D_ID_FLAG = 0
I_ID = ''

# Get the Data
for file in FILES:
    infile = open(file,"r")
    while infile:
        line = infile.readline()
        if DEBUG : print line
        s = line.split()
        if DEBUG : print s
        n = len(s)
        if (n==0 and FLAG_PATH == 1) :
                FLAG_PATH = 0
                D_ID_FLAG = 0

    

        for type1 in TP:
#        if (n>1) : x.execute (" INSERT INTO element (name,type,path,line_start,line_end) VALUES (%s,%s,%s,%s,%s) ", (s[0],s[1], s[2], s[3],s[4]))
            if (n>1 and s[0] == type1) :
                x.execute (" INSERT INTO element (name,type) VALUES (%s,%s) ", (s[1],s[0]))
                if ( s[0] == "D:") :
                    x.execute("SELECT id FROM element WHERE name = %s", s[1])
                    row = x.fetchone()
                    D_ID = row [0]
                    D_ID_FLAG = 1
                else :
                    x.execute("SELECT id FROM element WHERE name = %s", s[1])
                    row = x.fetchone()
                    I_ID = row [0]
                    x.execute (" INSERT INTO call_tree (d_id,i_id) VALUES (%s,%s) ", (D_ID,I_ID))
                    


        for type2 in TP1:
            if (n>1 and s[0] == type2 and FLAG_PATH == 0) :
                PATH = s[1]
                FLAG_PATH = 1
            elif (n>1 and s[0] == type2 and FLAG_PATH == 1) :
                if (n>1) : x.execute (" UPDATE element SET path = %s, line_start = %s ,line_end = %s  WHERE  name=%s ", ( PATH, s[2], s[3], s[1]))


#x.execute("SELECT *  FROM element")
#row = x.fetchall()
#print row
conn.close()



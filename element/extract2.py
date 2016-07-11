#!/usr/bin/env python


#Server Connection to MySQL:

import MySQLdb
import os

DEBUG = 0
FILES = ["Code_out.map"]
REG = '%linux%'
P_FLAG = ''

conn = MySQLdb.connect(host= "localhost",
                  user="root",
                  passwd="",
                  db="emmcfs")
x = conn.cursor()
#y = conn.cursor()


# Get the Data
for file in FILES:
    outfile = open(file,"w")


#    x.execute("SELECT id, type, name  FROM element WHERE path IS NULL" )
    x.execute("SELECT id, type, name  FROM element WHERE type = '\D:\' and ( path LIKE \'%emmcfs%\' or path is NULL) " )
    row = x.fetchall() 
    for str1 in row :
        if DEBUG : print str1
        if str1[1] == 'P:' : break
        outfile.write( "\n" )
        outfile.write( str1[1] )
        outfile.write( " " )
        outfile.write( str1[2] )
        outfile.write( "\n" )
        if str1[1] == 'D:' :
            if DEBUG : print str1[0]
            x.execute("SELECT i_id  FROM call_tree WHERE d_id = %s ", str1[0] )
            row1 = x.fetchall()
            if row1 :
                for str2 in row1 :
                    x.execute("SELECT id, type, name  FROM element WHERE id = %s ", str2[0] )
                    row2 = x.fetchall()
                    for str3 in row2:
                        if str3[1] == 'D:' : break
                        outfile.write( str3[1] )
                        outfile.write( " " )
                        outfile.write( str3[2] )
                        outfile.write( "\n" )

        outfile.write( "\n" )


    x.execute("SELECT name, path, line_start, line_end  FROM element WHERE path LIKE '%emmcfs%' " )
    row3 = x.fetchall()
    for str4 in row3:
        if P_FLAG != str4[1]:
            outfile.write("\nP: ")
            outfile.write(str4[1])
            outfile.write("\n")
            P_FLAG = str4[1]
        outfile.write( 'L:' )
        outfile.write( " " )
        outfile.write( str4[0] )
        outfile.write( " " )
        outfile.write( "%s" % str4[2] )
        outfile.write( " " )
        outfile.write( "%s" % str4[3] )
        outfile.write( "\n" )

    
    outfile.close()






conn.close()

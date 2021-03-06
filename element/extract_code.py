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
#    x.execute("SELECT id, type, name, path, code  FROM element WHERE type = %s ", 'D:' )
    x.execute("SELECT id, type, name, path, code  FROM element")
    row = x.fetchall() 
    for str1 in row :
        if DEBUG : print str1
        #if str1[1] == 'P:' : break
	#if str( str1[3] ) == 'None' : break
        outfile.write( str1[1] )
        outfile.write( "\t" )
        outfile.write( str1[2] )
        outfile.write( "\n" )
	if (str( str1[3] ) != 'None') :
		outfile1 = open("/home/ignat99" + str (str1[3]), "a")
		outfile1.write( str1[2] )
        	outfile1.write( "{\n\t" )
		print str1[4]
        	outfile1.write( str( str1[4] ) )
        	outfile1.write( "\n}\n" )
		outfile1.close()
	
        if str1[1] == 'D:' :
            if DEBUG : print str1[0]
            x.execute("SELECT i_id  FROM call_tree WHERE d_id = %s ", str1[0] )
            row1 = x.fetchall()
            if row1 :
                for str2 in row1 :
                    x.execute("SELECT id, type, name  FROM element WHERE id = %s ", str2[0] )
                    row2 = x.fetchall()
                    for str3 in row2:
                        outfile.write( str3[1] )
                        outfile.write( "\t" )
                        outfile.write( str3[2] )
                        outfile.write( "\n" )

        outfile.write( "\n" )


    x.execute("SELECT name, path, line_start, line_end  FROM element WHERE path IS NOT NULL ORDER BY path " )
    row3 = x.fetchall()
    for str4 in row3:
        if P_FLAG != str4[1]:
            outfile.write("P:\t")
            outfile.write(str4[1])
            outfile.write("\n")
            P_FLAG = str4[1]
        outfile.write( 'L:' )
        outfile.write( "\t" )
        outfile.write( str4[0] )
        outfile.write( "\t" )
        outfile.write( "%s" % str4[2] )
        outfile.write( "\t" )
        outfile.write( "%s" % str4[3] )
        outfile.write( "\n" )

    
    outfile.close()






conn.close()

#!/usr/bin/env python3
'''################################################################################### 
Name:		  createSipXMLFromDB.py
Associated Files: [createSipXMLFromDB.py, alcatel_template.xml, clientSipUserData.db ]
Description:	  This program reads sip user data details from a database and creates
                  a sip device config file from a template.
######################################################################################
'''
#PROGRAM DEPENDENCIES
import os
import sys
import fileinput
import sqlite3 as lite

#BGN CONFIG SETTINGS
''' db   '''
to_the_source_database		= 'db/clientSipUserData.db'
an_sql_query_on_a_table		= 'SELECT * FROM accounts'
''' file '''
the_template_file		= 'templates/alcatel_template.xml'
the_file_extension		= '_alcatel.xml'
the_output_folder		= 'outputfiles/'
''' template '''
the_template_username		= '[username_template]'
the_template_password		= '[password_template]'
the_template_sip_server		= '[sip_server_template]'
the_template_outbound_proxy	= '[outbound_proxy_template]'
''' sip  '''
the_username			= "Username"
the_password 			= "Password"
the_sip_server			= '192.168.1.101'
the_outbound_proxy		= '8.8.8.8'

#END CONFIG SETTINGS

#OPEN THE DB CONNECTION
conn = lite.connect(to_the_source_database)

with conn:
    #READ THE DATA FROM THE TABLE
    conn.row_factory	= lite.Row
    c			= conn.cursor()
    c.execute(an_sql_query_on_a_table )
    rows		= c.fetchall()
    for row in rows:
        #ROW VARIABLE MATCHING
        with_the_db_username		= row[the_username]
        with_the_db_password		= row[the_password]
        with_the_db_sip_server		= the_sip_server
        with_the_db_outbound_proxy	= the_outbound_proxy 

        #LOAD THE TEMPlATE FILE
        filedata = None
        with open(the_template_file, 'r') as file:
           filedata = file.read()

        #REPLACE THE TEMPLATE PARAMETERS
        filedata = filedata.replace(the_template_username,	 with_the_db_username      )
        filedata = filedata.replace(the_template_password,	 with_the_db_password      )
        filedata = filedata.replace(the_template_sip_server,	 with_the_db_sip_server    )
        filedata = filedata.replace(the_template_outbound_proxy, with_the_db_outbound_proxy)

        #WRITE THE DEVICE CONFIG FILE
        the_output_file = the_output_folder + with_the_db_username + the_file_extension
        with open(the_output_file, 'w') as file:
           file.write(filedata)

#CLOSE THE DB CONNECTION
conn.close()

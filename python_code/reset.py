#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'hlugo', 'pass12345', 'destiny');

with con:

	cur = con.cursor()
	cur.execute("DROP DATABASE destiny")
	cur.execute("CREATE DATABASE destiny")
	cur.execute("USE destiny")

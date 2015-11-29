#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'hlugo', 'pass12345', 'destiny');

with con:

	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS Clan")
	cur.execute("CREATE TABLE Clan(clanName VARCHAR(35) PRIMARY KEY, Size INT, Founder VARCHAR(20), Motto VARCHAR(50))")
	cur.execute("INSERT INTO Clan(clanName, Size, Founder, Motto) VALUES('Lords of War', 5, 'WildHeck', 'Never Stop Shooting')")

	cur.execute("DROP TABLE IF EXISTS Server")
	cur.execute("CREATE TABLE Server(serverID INT PRIMARY KEY, Location VARCHAR(25), Status VARCHAR(7))")

	cur.execute("DROP TABLE IF EXISTS Player")
	cur.execute("CREATE TABLE Player(gamerID VARCHAR(20) PRIMARY KEY, firstName VARCHAR(12), lastName VARCHAR(18), DOB DATE NOT NULL, age INT, gender VARCHAR(6))")


	cur.execute("DROP TABLE IF EXISTS playerCharacter")
	cur.execute("CREATE TABLE playerCharacter(race VARCHAR(6), gender VARCHAR(6), class VARCHAR(7), PRIMARY KEY (race, gender, class), light INT, strength INT, intelligence INT, discipline INT)")

	cur.execute("DROP TABLE IF EXISTS Vault")
	cur.execute("CREATE TABLE Vault(storedArmor VARCHAR, storedWeapons VARCHAR, storedItems VARCHAR)")

	cur.execute("DROP TABLE IF EXISTS LegArmor")
	cur.execute("CREATE TABLE LegArmor(legName VARCHAR(20), class VARCHAR(7), PRIMARY KEY(legName, class), rarity VARCHAR(10), def INT, dis INT, inte INT, str INT)")

	cur.execute("DROP TABLE IF EXISTS Gauntlets")
	cur.execute("CREATE TABLE Gauntlets(gauntletName VARCHAR(20), class VARCHAR(7), PRIMARY KEY(gauntletName, class), rarity VARCHAR(10), def INT, dis INT, inte INT, str INT)")

	cur.execute("DROP TABLE IF EXISTS ChestArmor")
	cur.execute("CREATE TABLE ChestArmor(chestName  VARCHAR(20), class VARCHAR(7), PRIMARY KEY(chestName, class), rarity VARCHAR(10), def INT, dis INT, inte INT, str INT)")

	cur.execute("DROP TABLE IF EXISTS Helmet")
	cur.execute("CREATE TABLE Helmet(helmName VARCHAR(20), class VARCHAR(7), PRIMARY KEY(helmName, class), rarity VARCHAR(10), def INT, dis INT, inte INT, str INT)")

	cur.execute("DROP TABLE IF EXISTS PrimaryWeapons")
	cur.execute("CREATE TABLE PrimaryWeapons(pName VARCHAR(20) PRIMARY KEY, rarity VARCHAR(10), damageType VARCHAR(10), subtype VARCHAR(20), attack INT)")

	cur.execute("DROP TABLE IF EXISTS SpecialWeapons")
	cur.execute("CREATE TABLE SpecialWeapons(sName VARCHAR(20) PRIMARY KEY, rarity VARCHAR(10), damageType VARCHAR(10), subtype VARCHAR(20), attack INT)")

	cur.execute("DROP TABLE IF EXISTS HeavyWeapons")
	cur.execute("CREATE TABLE HeavyWeapons(hName VARCHAR(20) PRIMARY KEY, rarity VARCHAR(10), damageType VARCHAR(10), subtype VARCHAR(20), attack INT)")

	cur.execute("DROP TABLE IF EXISTS Quests")
	cur.execute("CREATE TABLE Quests(title VARCHAR(20) PRIMARY KEY, rewards VARCHAR, source VARCHAR)")

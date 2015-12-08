#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'hlugo', 'pass12345', 'destiny');

with con:

	cur = con.cursor()
#Clan +
	cur.execute("CREATE TABLE Clan(clanName VARCHAR(35) PRIMARY KEY, Size INT NOT NULL, Founder VARCHAR(20) NOT NULL, Motto VARCHAR(50))")
#Server  +		
	cur.execute("CREATE TABLE Server(serverID INT PRIMARY KEY, Location VARCHAR(25) NOT NULL, Status VARCHAR(7) NOT NULL)")
#Player	+
	cur.execute("CREATE TABLE Player(gamerID VARCHAR(20) PRIMARY KEY, serverID INT NOT NULL, clanName VARCHAR(35), firstName VARCHAR(12) NOT NULL, lastName VARCHAR(18) NOT NULL, DOB DATE NOT NULL, age INT, gender VARCHAR(6) NOT NULL, FOREIGN KEY (serverID) REFERENCES Server(serverID), FOREIGN KEY (clanName) REFERENCES Clan(clanName))")
#pCharacter	+
	cur.execute("CREATE TABLE pCharacter(gamerID VARCHAR(20), FOREIGN KEY(gamerID) REFERENCES Player(gamerID), characterNum INT(1) NOT NULL,level INT NOT NULL, race VARCHAR(6) NOT NULL, gender VARCHAR(6) NOT NULL, class VARCHAR(7) NOT NULL, light INT DEFAULT 0, UNIQUE(gamerID, characterNum))")
#Vault	+
	cur.execute("CREATE TABLE Vault(gamerID VARCHAR(20) NOT NULL, FOREIGN KEY(gamerID) REFERENCES Player(gamerID), glimmer INT, legendaryMarks INT, silver INT)")
#Vault Items	+
	cur.execute("CREATE TABLE VaultItems(gamerID VARCHAR(20) NOT NULL, FOREIGN KEY(gamerID) REFERENCES Player(gamerID), itemName VARCHAR(25), quantity int)")
#LegArmor	+
	cur.execute("CREATE TABLE LegArmor(legName VARCHAR(40), class VARCHAR(7), PRIMARY KEY(legName, class), rarity VARCHAR(10), def INT, dis INT, inte INT, str INT)")
#Gauntlets	+
	cur.execute("CREATE TABLE Gauntlets(gauntletName VARCHAR(40), class VARCHAR(7), PRIMARY KEY(gauntletName, class), rarity VARCHAR(10), def INT, dis INT, inte INT, str INT)")
#ChestArmor	+
	cur.execute("CREATE TABLE ChestArmor(chestName  VARCHAR(40), class VARCHAR(7), PRIMARY KEY(chestName, class), rarity VARCHAR(10), def INT, dis INT, inte INT, str INT)")
#Helmet	+
	cur.execute("CREATE TABLE Helmet(helmName VARCHAR(40), class VARCHAR(7), PRIMARY KEY(helmName, class), rarity VARCHAR(10), def INT, dis INT, inte INT, str INT)")
#PrimaryWeapons  +
	cur.execute("CREATE TABLE PrimaryWeapons(pName VARCHAR(25) PRIMARY KEY, rarity VARCHAR(10), subtype VARCHAR(20), attack INT)")
#SpecialWeapons  +
	cur.execute("CREATE TABLE SpecialWeapons(sName VARCHAR(25) PRIMARY KEY, rarity VARCHAR(10), subtype VARCHAR(20), attack INT)")
#HeavyWeapons  +
	cur.execute("CREATE TABLE HeavyWeapons(hName VARCHAR(25) PRIMARY KEY, rarity VARCHAR(10), subtype VARCHAR(20), attack INT)")
#Quests  +
	cur.execute("CREATE TABLE Quests(title VARCHAR(35) PRIMARY KEY, steps INT, description VARCHAR(140), category VARCHAR(30))")
#Quest Rewards   +
	cur.execute("CREATE TABLE QuestRewards(title VARCHAR(35), reward VARCHAR(35), FOREIGN KEY(title) REFERENCES Quests(title), UNIQUE(title, reward))")
#InProgress Multivalued Attributes +
	cur.execute("CREATE TABLE InProgress(gamerID VARCHAR(20), characterNum INT, FOREIGN KEY (gamerID, characterNum) REFERENCES pCharacter(gamerID, characterNum), title VARCHAR(35), FOREIGN KEY (title) REFERENCES Quests(title), Unique(gamerID, characterNum, title))")
#equipedWeapons +
	cur.execute("CREATE TABLE equipedWeapons(gamerID VARCHAR(20), FOREIGN KEY (gamerID) REFERENCES Player(gamerID), characterNum INT, UNIQUE(gamerID, characterNum), pName VARCHAR(25), FOREIGN KEY (pName) REFERENCES PrimaryWeapons(pName), sName VARCHAR(25), FOREIGN KEY (sName) REFERENCES SpecialWeapons(sName), hName VARCHAR(25), FOREIGN KEY (hName) REFERENCES HeavyWeapons(hName), wLight INT DEFAULT 0)")
#equipedArmor +
	cur.execute("CREATE TABLE equipedArmor(gamerID VARCHAR(20), FOREIGN KEY (gamerID) REFERENCES Player(gamerID), characterNum INT, UNIQUE(gamerID, characterNum), class VARCHAR(7), helmName VARCHAR(40), FOREIGN KEY (helmName) REFERENCES Helmet(helmName), gauntletName VARCHAR(40), FOREIGN KEY (gauntletName) REFERENCES Gauntlets(gauntletName), chestName VARCHAR(40), FOREIGN KEY (chestName) REFERENCES ChestArmor(chestName), legName VARCHAR(40), FOREIGN KEY (legName) REFERENCES LegArmor(legName), aLight INT DEFAULT 0)")

	cur.execute("CREATE TRIGGER ageCalc BEFORE INSERT ON Player FOR EACH ROW BEGIN SET NEW.age = (YEAR(CURDATE())-YEAR(NEW.DOB)); END;")

	cur.execute("CREATE TRIGGER wLightAdd BEFORE INSERT ON equipedWeapons FOR EACH ROW BEGIN SET NEW.wLight = ((SELECT attack FROM PrimaryWeapons WHERE pName=NEW.pName)+(SELECT attack FROM SpecialWeapons WHERE sName=NEW.sName)+(SELECT attack FROM HeavyWeapons WHERE hName=NEW.hName)); END;")

	cur.execute("CREATE TRIGGER aLightAdd BEFORE INSERT ON equipedArmor FOR EACH ROW BEGIN SET NEW.aLight = ((SELECT def FROM Helmet WHERE helmName=NEW.helmName AND class=NEW.class)+(SELECT def FROM Gauntlets WHERE gauntletName=NEW.gauntletName AND class=NEW.class)+(SELECT def FROM ChestArmor WHERE chestName=NEW.chestName AND class=NEW.class)+(SELECT def FROM LegArmor WHERE legName=NEW.legName AND class=NEW.class)); END;")

	cur.execute("CREATE TRIGGER lightCalc BEFORE INSERT ON pCharacter FOR EACH ROW BEGIN SET NEW.light = (((SELECT wLight FROM equipedWeapons WHERE gamerID=NEW.gamerID AND characterNum=NEW.characterNum)+(SELECT aLight FROM equipedArmor WHERE gamerID=NEW.gamerID AND characterNum=NEW.characterNum))/7); END;")

#creating view for character searches
	cur.execute("CREATE VIEW charView AS SELECT pCharacter.gamerID, clanName, level, race, class, light FROM pCharacter, Player WHERE pCharacter.gamerID = Player.gamerID;")

	cur.execute("CREATE VIEW charBuild AS SELECT pCharacter.gamerID, pCharacter.characterNum, pCharacter.class, pName, sName, hName, light, helmName, gauntletName, chestName, legName FROM pCharacter, equipedWeapons, equipedArmor WHERE pCharacter.gamerId=equipedWeapons.gamerID AND equipedWeapons.gamerID=equipedArmor.gamerID AND pCharacter.characterNum=equipedWeapons.characterNum AND equipedWeapons.characterNum=equipedArmor.characterNum;")
	
	cur.execute("CREATE VIEW gamerQuests AS SELECT pCharacter.gamerID, pCharacter.characterNum, level, race, class, title FROM pCharacter, InProgress WHERE pCharacter.gamerID=InProgress.gamerID AND pCharacter.characterNum=InProgress.characterNum;")

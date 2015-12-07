#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import csv

with open('servers.csv', 'rb') as fin:
	reader = csv.DictReader(fin, )
	serversInput = [(i['serverID'], i['Location'], i['Status']) for i in reader]

clans = [
	('Cresent Night Wolves', 6, 'wildheck', 'Never Stop Shooting'),
	('Hunters of Destiny', 10, 'HoD Deadeye', 'Largest Community of Hunters in the World'),
	('Shadow Ravens', 4, 'XxMrHollywood', 'Forged in the fiery crucible of war'),
	('AngryArmy', 7, 'AngryJoeShow', 'Never Give Up! Never Surrender! Victory or DEATH!'),
	('Dads of Destiny', 5, 'Kingpin2', 'A Community For Gaming Dads'),
	('ForgeWorld', 7, 'JonnyOThan', ''),
	('PS4 Rad Raiders', 5, 'Cruciamen', 'All helpful players are welcome!'),
	('Guardians of the Galaxy', 12, 'Da6Beast8', 'We are Groot'),
	('Legends of the Clans', 4, 'abandon_all_hope', 'One Clan to Rule Them All'),
	('Shadow Forged Council', 6, 'Guledan', 'Born in Darkness'),
	('Laughin Coffin', 5, 'Red_Eye_Xaxa', 'We are the Red Guild'),
	('Knights of the Blood', 8, 'Heathcliff', 'Together we prevail'),
	('Justice League', 9, 'Batman', 'United we are stronger')
]

with open('players.csv', 'rb') as fin:
	reader = csv.DictReader(fin, )
	playerInput = [(i['gamerID'], i['serverID'], i['clanName'], i['firstName'], i['lastName'], i['DOB'], i['gender']) for i in reader]

with open('primary.csv', 'rb') as fin:
	reader = csv.DictReader(fin, )
	primaryInput = [(i['pName'], i['rarity'], i['subtype'], i['attack']) for i in reader]

with open('special.csv', 'rb') as fin:
	reader = csv.DictReader(fin, )
	specialInput = [(i['sName'], i['rarity'], i['subtype'], i['attack']) for i in reader]

with open('heavy.csv', 'rb') as fin:
	reader = csv.DictReader(fin, )
	heavyInput = [(i['hName'], i['rarity'], i['subtype'], i['attack']) for i in reader]

with open('helmet.csv', 'rb') as fin:
	reader = csv.DictReader(fin, )
	helmetInput = [(i['helmName'], i['class'], i['rarity'], i['def'], i['dis'], i['inte'], i['str']) for i in reader]

with open('gauntlets.csv', 'rb') as fin:
	reader = csv.DictReader(fin, )
	gauntletInput = [(i['gauntletName'], i['class'], i['rarity'], i['def'], i['dis'], i['inte'], i['str']) for i in reader]

with open('chest.csv', 'rb') as fin:
	reader = csv.DictReader(fin, )
	chestInput = [(i['chestName'], i['class'], i['rarity'], i['def'], i['dis'], i['inte'], i['str']) for i in reader]

with open('legs.csv', 'rb') as fin:
	reader = csv.DictReader(fin, )
	legsInput = [(i['legName'], i['class'], i['rarity'], i['def'], i['dis'], i['inte'], i['str']) for i in reader]

with open('quests.csv', 'rb') as fin:
	reader = csv.DictReader(fin, )
	questInput = [(i['title'], i['steps'], i['description'], i['category']) for i in reader]

with open('questRewards.csv', 'rb') as fin:
	reader = csv.DictReader(fin, )
	rewardInput = [(i['title'], i['reward']) for i in reader]

with open('characters.csv', 'rb') as fin:
	reader = csv.DictReader(fin, )
	charactersInput = [(i['gamerID'], i['characterNum'], i['level'], i['race'], i['gender'], i['class']) for i in reader]

with open('equipedWeapons.csv', 'rb') as fin:
	reader = csv.DictReader(fin, )
	ewInput = [(i['gamerID'], i['characterNum'], i['pName'], i['sName'], i['hName']) for i in reader]

with open('equipedArmor.csv', 'rb') as fin:
	reader = csv.DictReader(fin, )
	eaInput = [(i['gamerID'], i['characterNum'], i['class'], i['helmName'], i['gauntletName'], i['chestName'], i['legName']) for i in reader]

con = mdb.connect('localhost', 'hlugo', 'pass12345', 'destiny');

with con:
	cur = con.cursor()
	cur.executemany("INSERT INTO Server(serverID, Location, Status) VALUES(%s, %s, %s)", serversInput)
	cur.executemany("INSERT INTO Clan(clanName, Size, Founder, Motto) VALUES(%s, %s, %s, %s)", clans)
	cur.executemany("INSERT INTO Player(gamerID, serverID, clanName, firstName, lastName, DOB, gender) VALUES(%s, %s, %s, %s, %s, %s, %s)", playerInput)
	cur.executemany("INSERT INTO PrimaryWeapons(pName, rarity, subtype, attack) VALUES(%s, %s, %s, %s)", primaryInput)
	cur.executemany("INSERT INTO SpecialWeapons (sName, rarity, subtype, attack) VALUES (%s, %s, %s, %s)", specialInput)
	cur.executemany("INSERT INTO HeavyWeapons (hName, rarity, subtype, attack) VALUES (%s, %s, %s, %s)", heavyInput)
	cur.executemany("INSERT INTO Helmet (helmName, class, rarity, def, dis, inte, str) VALUES (%s, %s, %s, %s, %s, %s, %s)", helmetInput)
	cur.executemany("INSERT INTO Gauntlets (gauntletName, class, rarity, def, dis, inte, str) VALUES (%s, %s, %s, %s, %s, %s, %s)", gauntletInput)
	cur.executemany("INSERT INTO ChestArmor (chestName, class, rarity, def, dis, inte, str) VALUES (%s, %s, %s, %s, %s, %s, %s)", chestInput)
	cur.executemany("INSERT INTO LegArmor (legName, class, rarity, def, dis, inte, str) VALUES (%s, %s, %s, %s, %s, %s, %s)", legsInput)
	cur.executemany("INSERT INTO Quests(title, steps, description, category) VALUES(%s, %s, %s, %s)", questInput)
	cur.executemany("INSERT INTO QuestRewards(title, reward) VALUES(%s, %s)", rewardInput)	
	cur.executemany("INSERT INTO equipedWeapons(gamerID, characterNum, pName, sName, hName) VALUES(%s, %s, %s, %s, %s)", ewInput)
	cur.executemany("INSERT INTO equipedArmor(gamerID, characterNum, class, helmName, gauntletName, chestName, legName) VALUES(%s, %s, %s, %s, %s, %s, %s)", eaInput)
	cur.executemany("INSERT INTO pCharacter(gamerID, characterNum, level, race, gender, class) VALUES(%s, %s, %s, %s, %s, %s)", charactersInput)

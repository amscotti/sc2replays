#! /usr/bin/env python

import MySQLdb
import sc2reader
# import os

replay_file = sc2reader.read_file("/home/mbedford/replays/Shakuras Plateau.SC2Replay")

filename = replay_file.filename
# filename = filename.replace(' ', '-')
#filename = "1"
player1 = replay_file.players[0].name
p1_race = replay_file.players[0].play_race
player2 = replay_file.players[1].name
p2_race = replay_file.players[1].play_race
map = replay_file.map
date_played = replay_file.date
# Format game length
if replay_file.length.hours:
	game_hours = "%sh" % replay_file.length.hours
else:
	game_hours = ""
if replay_file.length.mins:
	game_mins = "%sm" % replay_file.length.mins
else:
	game_mins = ""
if replay_file.length.secs:
	game_secs = "%ss" % replay_file.length.secs
else:
	game_secs = ""
game_length = "%s %s %s" % (game_hours,game_mins,game_secs)
#find winner
if replay_file.players[0].result == "Win":
	winner = player1
elif replay_file.players[1].result == "Win":
	winner = player2
# winner = replay_file.winner
patch_ver = replay_file.release_string
format = replay_file.type
game_category = replay_file.category

db_con = MySQLdb.connect(user='sc2replays', db='sc2replays', passwd='m34tba!!$', host='localhost')
cursor = db_con.cursor()


insert_query = 'INSERT INTO display_replays (file, player1, player2, p1_race, p2_race, map_name, date_played, game_length, winner, patch_ver, format, game_category) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s");' % (filename, player1, player2, p1_race, p2_race, map, date_played, game_length, winner, patch_ver, format, game_category)

print insert_query

cursor.execute (insert_query)
print "Number of rows inserted: %d" % cursor.rowcount
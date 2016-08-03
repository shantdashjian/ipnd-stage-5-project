# README for Intro to Programming Nanodegree: Choose Your Path: Back-End Developer Final Project
## Developer: Shaun Dashjian
## Date: 08.02.2016

### To Run The Code:
1. In psql console, import `tournament.sql`:
```
=> \i tournament.sql
CREATE DATABASE
You are now connected to database "tournament" as user "vagrant".
CREATE TABLE
CREATE TABLE
CREATE VIEW
CREATE VIEW
CREATE VIEW
CREATE VIEW
CREATE VIEW
=>
```
2. In Terminal, run the `tournament_test.py` unit test suite:
```
$ python tournament_test.py
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.

8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
$
```

### Credit:
I learned how to use *correlated subquerries* from various **stackoverflow.com** posts.

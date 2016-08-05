#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    try:
        connection = psycopg2.connect("dbname={}".format(database_name))
        cursor = connection.cursor()
        return connection, cursor
    except:
        print ("Database connection could't get established")


def deleteMatches():
    """Remove all the match records from the database."""
    connection, cursor = connect()
    sql = "delete from matches;"
    cursor.execute(sql)
    connection.commit()
    connection.close()

def deletePlayers():
    """Remove all the player records from the database."""
    connection, cursor = connect()
    sql = "delete from players;"
    cursor.execute(sql)
    connection.commit()
    connection.close()

def countPlayers():
    """Returns the number of players currently registered."""
    connection, cursor = connect()
    sql = "select count(*) from players;"
    cursor.execute(sql)
    count = cursor.fetchone()[0]
    connection.close()
    return count

def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    connection, cursor = connect()
    sql = 'insert into players (name) values(%s);'
    parameter = (name,)
    cursor.execute(sql, parameter)
    connection.commit()
    connection.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    connection, cursor = connect()
    sql = "select id, name, wins, matches from standings;"
    cursor.execute(sql)
    player_standings = cursor.fetchall()
    connection.close()
    return player_standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    connection, cursor = connect()
    sql = 'insert into matches (winner, loser) values(%s, %s);'
    parameters = (winner, loser,)
    cursor.execute(sql, parameters)
    connection.commit()
    connection.close()

def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    connection, cursor = connect()
    sql = '''select odd_standings.id as id1, odd_standings.name as name1,
        even_standings.id as id2, even_standings.name as name2
        from odd_standings, even_standings where odd_standings.pairing = even_standings.pairing;
    '''
    cursor.execute(sql)
    player_standings = cursor.fetchall()
    connection.close()
    return player_standings

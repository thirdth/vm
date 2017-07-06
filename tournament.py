#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import sys


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection, or
    it prints the relevant error message."""
    try:
        return psycopg2.connect("dbname=tournament")

    except:
        print('An error occured connecting to the database "tournament".')
        sys.exit()


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    # Clears the "matches" table, but does not get rid of the table.
    c.execute("delete from matches;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    # Clears the "players" table, but does not get rid of the table.
    c.execute("delete from players;")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    # Counts the number of entries in the "players" table.
    c.execute("select count(*) as num from players;")
    num = c.fetchone()[0]
    conn.commit()
    conn.close()
    return num


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    # Inserts a players name into the "players" table.
    c.execute("INSERT INTO players (name) VALUES (%s);", (str(name), ))
    conn.commit()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    # Gets all the information from the view "standings".
    c.execute("SELECT * from standings;")
    result = c.fetchall()
    conn.close()
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    # Inserts "winner_id" and "loser_id" into the table "matches"
    c.execute("INSERT INTO matches (winner_id, loser_id) VALUES (%s,%s)",
              (winner, loser))
    conn.commit()
    conn.close()


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
    conn = connect()
    c = conn.cursor()
    """ This query takes the views odd and even and gets the name and id of each
    player and joining these two views on the row number to return the propper
    tupples."""
    c.execute(" SELECT even.id, even.name, odd.id, odd.name\
    from even\
    inner join odd on even.row = odd.row;\
    ")
    pairings = c.fetchall()
    conn.commit()
    conn.close()
    return pairings

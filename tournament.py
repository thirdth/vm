#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    posts = c.execute("delete from matches;")
    conn.commit()
    conn.close()
    return posts


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("delete from players;")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    posts = c.execute("select count(*) as num from players;")
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
    c.execute("INSERT INTO players (name) VALUES (%s);", (str(name), ))
    conn.commit()

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
    conn = connect()
    c = conn.cursor()
    c.execute("CREATE or REPLACE VIEW standings AS\
        SELECT players.id, players.name,\
        (SELECT count(matches.winner_id)\
        FROM matches\
        WHERE players.id = matches.winner_id)\
        AS total_wins,\
        (SELECT count (matches.id)\
        FROM matches\
        WHERE players.id = matches.winner_id\
        OR players.id = matches.loser_id)\
        AS total_matches\
        FROM players\
        ORDER BY total_wins DESC, total_matches DESC;\
        select * from standings;")
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
    c.execute("INSERT INTO matches (winner_id, loser_id) VALUES (%s,%s)", (winner, loser))
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
    c.execute("CREATE or REPLACE VIEW player_order AS\
    SELECT id, name, total_wins,\
    row_number() over(order by total_wins) as game\
    from standings;\
    create or REPLACE view even as\
    select id, name,\
    row_number() over(order by game) as row\
    from player_order\
    where game % 2 = 0;\
    create or REPLACE view odd as\
    select id, name,\
    row_number() over(order by game) as row\
    from player_order\
    where game % 2 != 0;\
    SELECT even.id, even.name, odd.id, odd.name\
    from even\
    inner join odd on even.row = odd.row;\
    ")
    pairings = c.fetchall()
    conn.commit()
    conn.close()
    return pairings

-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Clears the database if it already exists, so we can start anew
DROP DATABASE if exists tournament;

-- Creates the database titled "tournament"
CREATE DATABASE tournament;

-- Connects to newly created database
\c tournament;

-- Creates a table called "players" with a name and id
CREATE TABLE players (
  id serial primary key,
  name text NOT NULL
);

-- Creates a table called "matches" with the information from each match
CREATE TABLE matches (
  id serial primary key,
  winner_id integer references players(id),
  loser_id integer references players(id)
);

/*This creates a view called Standings by connecting the
name and id in the Players table with how many wins that player has
and how many matches that player has played in the Matches table.*/
CREATE or REPLACE VIEW standings AS
      SELECT players.id, players.name,
      (SELECT count(matches.winner_id)
      FROM matches
      WHERE players.id = matches.winner_id)
      AS total_wins,
      (SELECT count (matches.id)
      FROM matches
      WHERE players.id = matches.winner_id
      OR players.id = matches.loser_id)
      AS total_matches
      FROM players
      ORDER BY total_wins DESC, total_matches DESC;

/* This ultimately creates three views in order to sort the information needed
for swissPairings() function in tournament.py; 'player_order', 'odd', and 'even'.
'Player_order' creates a view using the view 'standings' where the players
are put in order of their ranking, numbered from 1 to N in sequential order.
'Odd' then creates a view using just the odd numbers from that 'player_order'
view and re-orders them from 1 to N, and 'even' takes all the even numbers from
'player_order' and does the same thing.*/
CREATE or REPLACE VIEW player_order AS
      SELECT id, name, total_wins,
      row_number() over(order by total_wins) as game
      from standings;
      create or REPLACE view even as
      select id, name,
      row_number() over(order by game) as row
      from player_order
      where game % 2 = 0;
      create or REPLACE view odd as
      select id, name,
      row_number() over(order by game) as row
      from player_order
      where game % 2 != 0;

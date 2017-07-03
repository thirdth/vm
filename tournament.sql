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
  name varchar(50) NOT NULL
);

-- Creates a table called "matches" with the information from each match
CREATE TABLE matches (
  id serial primary key,
  p_one_id integer references players(id),
  p_two_id integer references players(id),
  winner_id integer references players(id),
  loser_id integer references players(id),
);

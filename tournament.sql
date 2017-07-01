-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE if exists tournament;

CREATE DATABASE tournament;

\c tournament;

CREATE TABLE players (
  id serial primary key,
  name varchar(50) NOT NULL
);

CREATE TABLE matches (
  id serial primary key,
  p_one_id integer references players(id),
  p_two_id integer references players(id),
  winner_id integer references players(id),
  loser_id integer references players(id),
  round_num integer
);



select * from players, matches;

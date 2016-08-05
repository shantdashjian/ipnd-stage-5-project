-- Table definitions for the tournament project.
--

-- Drop database if already exists, create the database, and connect to it
DROP DATABASE IF EXISTS tournament;
create database tournament;
\c tournament

-- Create the tables
create table players (
  id serial PRIMARY KEY,
  name text
);

create table matches (
  id serial PRIMARY KEY,
  winner int references players(id),
  loser int references players(id)
);

create view player_wins as
  select id, (select count(*) from matches where winner = p.id) wins from players p;

create view player_matches as
  select id, (select count(*) from matches where winner = p.id or loser = p.id) matches from players p;

create view standings as
  select players.id as id, name, wins, matches from players, player_wins, player_matches where players.id = player_wins.id and player_wins.id = player_matches.id order by wins;

create view odd_standings as
  select inner_pairing / 2 + 1 as pairing, id, name from (
    select row_number() over() as inner_pairing, id, name
    from standings
  ) as dummy
  where mod(inner_pairing, 2) = 1;

  create view even_standings as
    select inner_pairing / 2 as pairing, id, name from (
      select row_number() over() as inner_pairing, id, name
      from standings
    ) as dummy
    where mod(inner_pairing, 2) = 0;

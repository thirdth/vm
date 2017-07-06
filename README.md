# Swiss Pairings Tournament database
Source code for a tournament results database utilizing the Swiss
Pairing system for **Full Stack Web Developer Nanodegree Program**
from **Udacity**

## Overview
This code allows for a tournament to be set up in a manner such that in each
successive round, the players are pitted against another player who has the same
or closest to the same number of wins as that player. The tournament continues
until there is only one undefeated player left in the tournament.

This database utilizes two tales, "players" and "matches", while the `tournament.py`
file allows the user to delete matches, delete players, count players, register
players, get player standings, report the outcome of a match, and get the
pairings for the next round.

## Set-up Instructions
1. This program is intended to be used from a command line environment utilizing
a virtual machine.
2. You will need to set-up a virtual machine like Virtual Box, and a way to connect
to that virtual machine, like with Vagrant. Instructions for set-up VirtualBox can be found [here](https://www.virtualbox.org/manual/https://www.vagrantup.com/intro/getting-started/ch01.html) While Instructions to download and set up Vagrant can be found [here](https://www.vagrantup.com/intro/getting-started/)
4. Prior to setting up Vagrant, download the files for the program onto your local machine.
5. Navigate to the folder containing these files and run `vagrant up` in order to
initialize your virtualMachine and connect to it through Vagrant. These files contain
a Vagrantfile that handles the set-up.
6. Once you have set-up Vagrant and Virtual Box you can utilize the database and
program through the command line in vagrant.
8. Navigate to the local folder that you set up Vagrant in, and run vagrant.ssh.
9. Navigate to your Tournament folder in the virtual machine through the Vagrant directory.
11. Run the command `psql` in order to start the database environment. If you get
an error, or postgreql is not set up on your computer look [here](http://www.techrepublic.com/blog/diy-it-guy/diy-a-postgresql-database-server-setup-anyone-can-handle/) for Instructions
on how to download it and how to set-up a postgresql database.
12. Once in the psql environment, run `\i tournament.sql` in order to create the
proper databases for this use.
13. Exit the psql database by running the command `\q`
10. Test that you have set-up everything correctly by running `python tournament_test.py`. If it returns no errors, then your environment is set up appropriately.
13. Once the tournament database is initialized, you can run your python file.

## Sample use
1. Create a `.py` file to edit in order to communicate with the database, and
import the `tournament.py` file into it in order to make use of the functions.
1. Create your players using the `registerPlayers()` function.
2. Once all your players are registered, use the `swissPairings()` function to
determine what the match-ups are for the current round.
3. After the matches have been played, use the `reportMatch()` function to enter
the results into the database.
4. Once all the results of a particular round are entered into the database, use
the `swissPairings()` function to get the match-ups for the next round.
5. Repeat steps 3 and 4 until only one player is left undefeated.
6. At any time, you can get the current standings from the database using the
`playerStandings()` function.
7. When you want to execute your program, run `python [your_file]` in the command
line.

## Known Issues
1. If there is a tie for first place, the `playerStandigns()` function has no way
of breaking that tie, and it will not show both players as first place, it will return them
as first place and second place.
2. Vagrantfile does not set-up postgresql properly, so it will be incumbent on
the user to download it and set it up in their machine using the link noted above
in **Step 11**. Later iterations of this will correct that bug.

# Visual Tic-Tac-Toe

Tic-Tac-Toc game that accept playing against a human or a computer.

Currently implemented random agent and montecarlo agent. The later is impossible to beat.

# Game play

> ./main.py

# Game settings

Most of the settings of the game can be changed in the script settings.py

In the section `match players` you can update the players that will play in the match.
PLAYER0 is the first player and PLAYER1 is the second. The should contain the name
of a valid player (i.e one name defined above, in the `player names` section). To add
new players see `Add custom player` below.

# Add custom player

To add a new player add a new script in the strategy folder that implements it.
The player must be a class that is initialized with a copy of an instance of the game.
It mush implement the method `getmove` that receives the current state of the game
and returns a position (x, y), the move to be done.

See `strategy/random.py` for an example.

To register your player you need to update the file strategy/__init__.py. Import your player
and update the PLAYER_NAMES dict. Optionally you can add your player name in the settings.py file or use it directly in one of the players.

# Credits

The pygame implementation was extracted from http://github.com/kgodey/pygame-tictactoe. I adapted it to my project in order to accept new programatic strategies. Also modes (Human VS Computer) and (Computer VS Computer) are valid.


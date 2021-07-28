# Genreal Info:
A Tic Tac Toe game created with Python 3.\
It uses a minimax agorithmn with alpha-beta prunning.

Mostly based on the sources: \
https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-3-tic-tac-toe-ai-finding-optimal-move/\
https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/?ref=lbp\
https://www.youtube.com/watch?v=l-hh51ncgDI\
https://www.hackerearth.com/blog/developers/minimax-algorithm-alpha-beta-pruning/\


# Notes to myself:

## Help from reddit:
- [method to randomly select a function](https://www.reddit.com/r/learnpython/comments/ofhke1/randomly_selecting_a_function_from_a_list/?utm_source=share&utm_medium=web2x&context=3)
```
playerOneTurn = random.choice([playHuman, playComputer])
playerTwoTurn = [playHuman, playComputer][playerOneTurn == playHuman]
```
- playerOneTurn is selected randomly from the list. Later, it select playerTwoTurn from a list by indexing it. As index it uses "playerOneTurn == playHuman" which results as bool variable. bool variables are integers in python so False is 0, True is 1. If playerOneTurn is playHuman it select first element from list which is playComputer.
- or just use:
``` 
playerTwoTurn = playComputer if playerOneTurn == playHuman else playHuman
```

- [had trouble with minimax function](https://www.reddit.com/r/algorithms/comments/oiolae/need_help_with_minimax_function_and/?utm_source=share&utm_medium=web2x&context=3)

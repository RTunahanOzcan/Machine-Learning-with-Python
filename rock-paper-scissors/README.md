# Rock Paper Scissors

My answer to the first project of Machine Learning with Tensorflow course of 'freecodecamp.com'.

## What’s the problem we’re solving?
We want to predict the opponent’s next move based on their past moves.

  *If they’re random, we can’t do better than 50% win rate.

  *But most opponents aren’t random — they show patterns (like repeating sequences or favoring certain moves).

  *If we can spot these patterns → we can counter them consistently. 
## What’s a Markov Chain?
A Markov chain is a model where:
  *The future state depends only on the recent past state(s), not the whole history. 
## How I apply it to RPS
1- Track opponet's moves in a history list.
2- Pick a markov order n (n is 3 in my case)
3- Build a dictionary requires frequency of moves.
4- Predict next move = The move that most often follows current state
5- Counter it.
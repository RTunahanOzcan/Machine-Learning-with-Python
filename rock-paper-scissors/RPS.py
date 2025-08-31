# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    n = 3

    counters = {"R": "P", "P": "S", "S": "R"}

    if len(opponent_history) > n:
        recent_pattern = "".join(opponent_history[-n:])

        patterns = {}
        for i in range(len(opponent_history) - n):
            seq = "".join(opponent_history[i:i+n])
            next_move = opponent_history[i+n]

            if seq not in patterns:
                patterns[seq] = {"R": 0, "P": 0, "S": 0}
            if next_move in ["R", "P", "S"]:
                patterns[seq][next_move] += 1

        if recent_pattern in patterns:
            prediction = max(patterns[recent_pattern],
                             key=patterns[recent_pattern].get)
            guess = counters[prediction]
        else:
            # Smarter fallback: weighted prediction from overall history
            counts = {"R": 0, "P": 0, "S": 0}
            for move in opponent_history:
                if move in counts:
                    counts[move] += 1
            if sum(counts.values()) > 0:
                prediction = max(counts, key=counts.get)
                guess = counters[prediction]
            else:
                guess = random.choice(["R", "P", "S"])
    else:
        # Very early fallback: play randomly to avoid being predictable
        guess = random.choice(["R", "P", "S"])
    return guess

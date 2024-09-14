# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], plays = {}):

    if prev_play == "":
        prev_play = 'R'

    opponent_history.append(prev_play)
    nextplay = 'S'

    if len(opponent_history) > 4:
        prevPlays = "".join(opponent_history[-5:])
        plays[prevPlays] = plays.get(prevPlays, 0) + 1

    plays_prediction = []

    for play in ['R','P','S']:
        prev4Plays = "".join(opponent_history[-4:] + play)
        plays_prediction.append(prev4Plays)



    return guess

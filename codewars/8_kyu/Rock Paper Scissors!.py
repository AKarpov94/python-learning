def rps(p1, p2):
    if (p1 == "scissors" and p2 == "paper") or ((p1 == "paper" and p2 == "rock")) or (p1 == "rock" and p2 == "scissors"):
        return "Player 1 won!"
    elif (p1 ==  p2):
        return "Draw!"
    else:
        return "Player 2 won!"
rps = rps("paper", "rock")
print(rps)

    #rps = rps("paper", "rock")
    #print(rps)
    #if rps == p1:
    #    return "Player 1 won!"
    #your code here
    #def rps(p1, p2):
    #    hand = {'rock': 0, 'paper': 1, 'scissors': 2}
    #    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    #    return results[hand[p1] - hand[p2]]

    #def rps(p1, p2):
    #    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    #    if beats[p1] == p2:
    #        return "Player 1 won!"
    #    if beats[p2] == p1:
    #        return "Player 2 won!"
    #    return "Draw!"

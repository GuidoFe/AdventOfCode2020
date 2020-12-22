
# round = 0


def subgame(decks):
    # global round
    pastRounds = []
    while len(decks[0]) != 0 and len(decks[1]) != 0:
        # round += 1
        # print("Round " + str(round))
        for pastRound in pastRounds:
            if pastRound[0] == decks[0] and pastRound[1] == decks[1]:
                # print("Found Loop returning to round " + str(pastRound[2]))
                # print("Current decks: " + str(decks))
                return 0
        pastRounds.append([decks[0].copy(), decks[1].copy(), round])
        # print("Deck of Player 1: " + str(decks[0]))
        # print("Deck of Player 2: " + str(decks[1]))
        cards = [decks[0].pop(), decks[1].pop()]
        # print("Player 1 draws " + str(cards[0]))
        # print("Player 2 draws " + str(cards[1]))
        if len(decks[0]) >= cards[0] and len(decks[1]) >= cards[1]:
            # print("Starting subgame...\n-------------------------------")
            winner = subgame([decks[0][-cards[0]:], decks[1][-cards[1]:]])
            loser = (winner + 1) % 2
            # print("Winner of subgame: " + str(winner + 1) + "\n---------------------------------")
        else:
            if cards[0] > cards[1]:
                winner = 0
                loser = 1
            else:
                winner = 1
                loser = 0
        # print("Winner of round: " + str(winner + 1))
        decks[winner].insert(0, cards[winner])
        decks[winner].insert(0, cards[loser])
    if len(decks[0]) == 0:
        # print("Player 2 wins subgame")
        return 1
    else:
        # print("Player 1 wins subgame")
        return 0


def main():
    f = open("input")
    decks = [[], []]
    currentPlayer = 0
    for line in f:
        line = line.strip()
        if line == "Player 1:":
            pass
        elif line == "Player 2:":
            currentPlayer = 1
        elif len(line) != 0:
            decks[currentPlayer].insert(0, int(line))
    winner = subgame(decks)
    score = 0
    for i, e in enumerate(decks[winner]):
        score += (i + 1) * e
    print(score)


main()

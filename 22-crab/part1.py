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
    while len(decks[0]) != 0 and len(decks[1]) != 0:
        cards = [decks[0].pop(), decks[1].pop()]
        if cards[0] > cards[1]:
            winner = 0
            loser = 1
        else:
            winner = 1
            loser = 0
        decks[winner].insert(0, cards[winner])
        decks[winner].insert(0, cards[loser])
    if len(decks[0]) == 0:
        winner = 1
    else:
        winner = 0
    score = 0
    for i, e in enumerate(decks[winner]):
        score += (i + 1) * e
    print(score)


main()

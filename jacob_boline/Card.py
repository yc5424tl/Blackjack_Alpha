

Suits = "Clubs Diamonds Hearts Spades".split()
Ranks = "Ace Two Three Four Five Six Seven Eight Nine Ten Jack Queen King".split()


class Card:

    def __init__(self, card_suit, card_rank):
        self.suit = card_suit
        self.rank = card_rank

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

    # def __getitem__(self, index):
    #     return self[index]

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

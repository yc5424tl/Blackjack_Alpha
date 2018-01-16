
class Shoe:

    def __init__(self):
        self.number_of_decks = 0
        self.cards_in_shoe = []
        self.discard_pile = []

    def __str__(self):
        print("Cards in shoe: \n")
        for card in self.cards_in_shoe:
            print(card.__str__())

    def remove_burn_card(self):
        card_removed = self.cards_in_shoe.pop(0)
        self.discard_pile.append(card_removed)

    def deal_card(self):
            return self.cards_in_shoe.pop(0)

    def show_burn_card(self):
        burn_card = self.discard_pile.pop(0)
        print('\n     ======  Burn Card: ' + burn_card.__str__() + '  ======\n\n')
        self.discard_pile.append(burn_card)

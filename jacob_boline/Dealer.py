import time


class Dealer:

    def __init__(self):
        self.hand = []
        self.name = 'The Dealer'

    def __str__(self):
        print('The Dealer')

    def add_card_to_hand(self, card):
        self.hand.append(card)
        time.sleep(.5)

    def clear_hand(self):
        self.hand.clear()

    def last_card_dealt(self):
        print(self.name + ' is dealt a ' + self.hand[-1].__str__())

from jacob_boline import Dealer


class Player(Dealer.Dealer):

    def __init__(self, player_name, bank_roll, seat_number):
        self.hand = []
        self.bank = bank_roll
        self.name = player_name
        self.bet = 0
        self.seat = seat_number

    def __str__(self):
        print("Player: " + self.name + '\n' +
              "Seat: " + str(self.seat) + '\n' +
              "Bank: " + str(self.bank))

    def get_seat_number(self):
        return self.seat

    def get_bank_total(self):
        return self.bank

    # def add_card_to_hand(self, card):
    #     self.hand.append(card)
    #
    # def clear_hand(self):
    #     self.hand.clear()


# TODO @ def clear_hand - adding to discard pile in order to reuse the entire shoe as opposed to creating new decks
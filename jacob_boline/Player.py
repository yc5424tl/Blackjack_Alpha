from jacob_boline import Dealer


class Player(Dealer.Dealer):

    def __init__(self, player_name, bank_roll, seat_number):
        super().__init__()
        self.hand = []
        self.split_hand = []
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


    def select_play_action(self):

        options_dict = {'SPLIT': False, **dict.fromkeys(['HIT', 'DOUBLE DOWN', 'STAY'], True)}

        if self.hand[0].get_rank() == self.hand[1].get_rank():
            options_dict['SPLIT'] = True

        if len(self.hand) > 2:
            options_dict['DOUBLE DOWN'] = False

        print('Options: ' + ', '.join([option for option in options_dict if options_dict.get(option) is True]))
        # for k, v in options_dict: if v is True, k will be presented as an option of play to the player

        while True:
            selection = input('\n     Enter an option to continue.\n')

            if selection.upper() in options_dict.keys() and options_dict.get(selection.upper()) is True:
                return selection.lower()
            else:
                continue




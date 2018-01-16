
class BlackjackTable:

    def __init__(self, minimum_bet, maximum_bet):
        assert (0 < minimum_bet < maximum_bet) and (maximum_bet % minimum_bet == 0)
        self.capacity = 7
        seats = [0, 1, 2, 3, 4, 5, 6]
        self.players = {seat: None for seat in seats}
        self.min_bet = minimum_bet
        self.max_bet = maximum_bet

    def __str__(self):
        print("There are currently " + str(len(self.players)) + ' of ' + str(self.capacity) + ' spots occupied.')

    def add_player(self, player):
        # seat_for_player = len(self.players)
        self.players[player.get_seat_number()] = player

    def remove_player(self, player):
        self.players[player.get_seat_number()] = None

    def number_of_players(self):
        player_count = 0
        for seat in self.players.keys():
            if self.players.get(seat) is not None:
                player_count += 1
        return player_count

    def get_open_seat_number(self):

        for seat in self.players.keys():
            if self.players.get(seat) is None:
                return seat




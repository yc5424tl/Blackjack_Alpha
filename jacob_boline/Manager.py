from jacob_boline import Dealer
from jacob_boline import Player, Deck, BlackjackTable, Shoe

shoe = Shoe.Shoe()
dealer = Dealer.Dealer()
table = BlackjackTable.BlackjackTable(5, 500)


def add_player():

    player_name = ''
    while player_name.strip() == '':
        player_name = input('Please enter your name.')
    seat_for_player = table.get_open_seat_number()
    table.add_player(Player.Player(player_name, 315, seat_for_player))


def seat_table():

    print('Welcome to Blackjack!')
    add_player()

    while True:
        additional_player = ''

        while additional_player.lower() != 'yes' or 'no':
            additional_player = input('Would you like to add another player? Enter YES or NO')

            if additional_player.lower() == 'yes':

                if table.number_of_players() == table.capacity:
                    print('Table is full, cannot add another player. Beginning game. ')
                    return False
                else:
                    add_player()

            elif additional_player.lower() == 'no':
                print('Beginning Game.')
                return False

            else:
                print('Uhh...yes or no?')


def get_number_of_decks():

    return len(table.players) + 1


def game_setup(number_of_decks):

    for i in range(number_of_decks):
        new_deck = Deck.Deck()
        new_deck.shuffle()
        for card in range(52):
            card_for_shoe = new_deck.deal_card()
            shoe.cards_in_shoe.append(card_for_shoe)

    shoe.remove_burn_card()
    shoe.show_burn_card()


def place_bet(player_up):

    while True:
        try:
            wager = int(input('Enter your bet'))
            while (table.max_bet < wager) or (wager % 1 != 0) or (wager > player_up.bank) or (wager < table.min_bet):
                if wager > player_up.bank:
                    print('Your bet cannot exceed your total funds of ' + str(player_up.bank))
                elif wager > table.max_bet:
                    print('Betting cannot exceed the table maximum of ' + str(table.max_bet))
                elif wager < table.min_bet:
                    print('Betting starts at the table minimum of ' + str(table.min_bet))
                elif wager % 1 != 0:
                    print('Betting can only be done in whole amounts.')
                wager = int(input('Enter your bet'))
            player_up.bet = wager
            print(player_up.name + ' placed a bet of ' + str(player_up.bet))
            break
        except ValueError:
            print('Whole Numerical Values Only Please')
            continue


def take_bets():
    for seat in table.players.keys():
        if table.players.get(seat) is not None:
            player_up = table.players.get(seat)
            place_bet(player_up)
    print('Bets Closed!')


def deal_cards():
    for deal in range(2):
        for seat in table.players.keys():
            if table.players.get(seat) is not None:
                table.players.get(seat).add_card_to_hand(shoe.deal_card())
                table.players.get(seat).last_card_dealt()
        dealer.add_card_to_hand(shoe.deal_card())
        if deal == 0:
            print('First Card to Dealer placed Face-Down')
        if deal == 1:
            dealer.last_card_dealt()


def main():

    seat_table()
    number_of_decks = get_number_of_decks()
    game_setup(number_of_decks)

    #start_game()
    take_bets()
    deal_cards()
    # offer_insurance()
    # check_dealer_blackjack()
    # player_actions()
    # dealer_action()


if __name__ == '__main__':
    main()

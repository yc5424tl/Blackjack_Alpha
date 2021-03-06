from jacob_boline import Dealer, Player, Deck, BlackjackTable, Shoe
from time import sleep

shoe = Shoe.Shoe()
dealer = Dealer.Dealer()
table = BlackjackTable.BlackjackTable(5, 500) # (min_bet, max_bet)


def add_player():

    player_name = ''
    while player_name.strip() == '':
        player_name = input('Please enter name.   \n')
    seat_for_player = table.get_open_seat_number()
    table.add_player(Player.Player(player_name, 315, seat_for_player))  # (name, default bank amount, seat)


def seat_table():

    print('Welcome to Blackjack!')
    add_player()

    while True:
        additional_player = ''

        while additional_player.lower() != 'yes' or 'no':
            additional_player = input('Would you like to add another player? Enter YES or NO   \n')

            if additional_player.lower() == 'yes':

                if table.number_of_players() == table.capacity:
                    print('Table is full, cannot add another player. Beginning game. \n')
                    return False
                else:
                    add_player()

            elif additional_player.lower() == 'no':
                print('\n=================  Beginning Game  =================')
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
                    # Takes input from a player to make a bet, validation for being whole, positive, within their funds, and within table limits.

                    #TODO either remove player, offer to increase bank, or quit game when a player's bank goes below the table min
    while True:
        try:
            print(player_up.name + ', your have ' + str(player_up.bank) + ' in your bank.')
            wager = int(input('     Enter your bet.   \n'))
            while (table.max_bet < wager) or (wager % 1 != 0) or (wager > player_up.bank) or (wager < table.min_bet):
                if wager > player_up.bank:
                    print('Your bet cannot exceed your total funds of ' + str(player_up.bank))
                elif wager > table.max_bet:
                    print('Betting cannot exceed the table maximum of ' + str(table.max_bet))
                elif wager < table.min_bet:
                    print('Betting starts at the table minimum of ' + str(table.min_bet))
                elif wager % 1 != 0:
                    print('Betting can only be done in whole amounts.')
                wager = int(input('\n' + player_up.name + ': Enter your bet   '))
            player_up.bet = wager
            print(player_up.name + ' placed a bet of ' + str(player_up.bet) + '\n')
            player_up.bank -= player_up.bet
            break
        except ValueError:
            print('\n     ***Whole Numerical Values Only Please***\n')
            continue


def take_bets():      # Loops through each player at the table, prompting for a bet.
    for seat in table.players.keys():
        if table.players.get(seat) is not None:
            player_up = table.players.get(seat)
            place_bet(player_up)
    print('\n        ==========  BETS CLOSED  ==========         \n\n')
    sleep(1)


def deal_cards():

    #TODO until a cut card feature is implemented, add a try/except to catch an empty shoe, show a final score?

    for deal in range(2):                   #  one card dealt to each player, and dealer,  twice around
        for seat in table.players.keys():
            if table.players.get(seat) is not None:
                table.players.get(seat).add_card_to_hand(shoe.deal_card())
                table.players.get(seat).last_card_dealt()
                print('\n')
                sleep(.5)
        dealer.add_card_to_hand(shoe.deal_card())
        if deal == 0:   # hide dealer's first card
            print('First Card to Dealer placed Face-Down \n\n')
            sleep(.5)
        if deal == 1:   # show dealer's second card
            dealer.last_card_dealt()
            #TODO  offer_insurance()
            if dealer.hand[-1].get_rank() in ['Ace', 'Ten', 'Jack', 'Queen', 'King']:
                if dealer.check_for_blackjack():  # check for dealer blackjack before play moves on.
                    print('Dealer turns over a ' + dealer.hand[0].__str__() + ' for a Blackjack!')
                    dealer.score = 100 # blackjack score
                    print('deal_cards() returning false')
                    return False
                else:
                    print('Dealer does NOT have a Blackjack.')
                    return True
            return True

        #### its a hash-tag party####

def player_action(action, player):

    if action == 'stay':
        print(player.name + ' stays with a ' + str(player.score))


    # add card from shoe to player hand, show card, score_hand will either end turn via bust/stay or offer any possible plays available
    if action == 'hit':
        player.add_card_to_hand(shoe.deal_card())
        player.last_card_dealt()
        player.score_hand()
        present_options(player)



    if action == 'split':
        print('STUB: player action == split')
        pass
        # TODO split logic
        # Split is being displayed under the correct conditions

    if action == 'double down':
        print('STUB: player action == double down')
        pass
        # TODO double down logic
        # double down is being presented under the correct conditions

def present_options(player):

    sleep(1)
    if player.score == 1:  # When a player busts, their score is set to 1 (for easy comparison). Here, this score will terminate the players turn.
        print(player.name + ' lost a bet of ' + str(player.bet))

    elif player.score == 21:   # Players are forced to stay with a score of 21
        player.show_hand()
        print(player.name + ' stays.')

    else:                   # If the above conditions are not met, the players will then be shown 'the table' along with a list of possible plays
        dealer.dealers_top_card()
        player.show_hand()
        selected_action = player.select_play_action()
        player_action(selected_action, player)


def start_player_turns():
    for seat in table.players.keys():
        if table.players.get(seat) is not None:
            player_up = table.players.get(seat)
            sleep(1)
            print("\n===== " + player_up.name.upper() + "'S TURN  =====\n")

            if player_up.check_for_blackjack():
                print(player_up.name + ' has a Blackjack!')
                player_up.score = 100      # arbitrary number assigned, only needed to be > 21

            else:                          #if no blackjack, player is presented with a list of possible plays to choose from
                present_options(player_up)


def get_results():
    for seat in table.players.keys():
        if table.players.get(seat) is not None:
            player = table.players.get(seat)
            sleep(1)
            if player.score == 1:
                print(player.name + "'s hand busted, losing " + str(player.bet))
            elif  player.score == 100 and player.score > dealer.score:   # checks for blackjack and that the dealer doesn't also have one
                print('Blackjack pays ' + player.name + ' at 2-to-1 for ' + str(player.bet * 2))
                player.bank += player.bet * 3     # returns original bet and the 2-1 payout
            elif player.score == dealer.score:
                print(player.name + "'s hand pushes, returning bet of " + str(player.bet) + ' to bank.')
                player.bank += player.bet   # bet returned to players bank
            elif dealer.score < player.score <= 21:
                print(player.name + "'s hand wins for " + str(player.bet))
                player.bank += player.bet * 2  # returns bet along with the equal amount in winnings
            elif 21 >= dealer.score > player.score:
                print(player.name + "'s hand loses on a wager of " + str(player.bet))   #no further action to the bank as the bet has already been removed
    print('\n\n      ======  STARTING NEXT HAND  ======      \n\n')
    sleep(2)

def clear_bets_and_scores():   # resets all scores, bets, and hands to zero/empty at the end of a round
    for seat in table.players.keys():
        if table.players.get(seat) is not None:
            player = table.players.get(seat)
            player.score = 0
            player.bet = 0
            player.hand = []
    dealer.clear_hand_and_score()







def main():

    seat_table()
    number_of_decks = get_number_of_decks()
    game_setup(number_of_decks)

    # start_game()
    while True:
        take_bets()
        if not deal_cards():
            get_results()
        else:
            start_player_turns()
            dealer.play_dealer_hand(shoe)
            get_results()
        clear_bets_and_scores()


if __name__ == '__main__':
    main()

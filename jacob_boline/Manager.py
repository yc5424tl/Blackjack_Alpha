from jacob_boline import Deck, Shoe, Card


def main():

    shoe = Shoe.Shoe()

    for x in range(3):  # produces 156 cards

        # 'TODO combine below in to an 'add deck to game' function 
        new_deck = Deck.Deck()
        new_deck.shuffle()
        for card in range(52):
            card_for_shoe = new_deck.deal_card()
            shoe.cards_in_shoe.append(card_for_shoe)

    shoe.remove_burn_card()
    shoe.show_burn_card()


if __name__ == '__main__':
    main()

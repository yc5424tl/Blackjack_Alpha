from jacob_boline import Deck, Shoe, Card


def main():

    shoe = Shoe.Shoe()

    for x in range(4):
        new_deck = Deck.Deck()
        new_deck.shuffle()
        shoe.add_deck(new_deck)

    # shoe.__str__()
    shoe.remove_burn_card()
    shoe.show_burn_card()


if __name__ == '__main__':
    main()

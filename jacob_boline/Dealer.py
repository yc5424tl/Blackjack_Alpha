import time

class Dealer:

    def __init__(self):
        self.hand = []
        self.name = 'The Dealer'
        self.score = 0

    def __str__(self):
        return self.name

    def add_card_to_hand(self, card):
        self.hand.append(card)
        time.sleep(.5)


    def clear_hand(self):
        self.hand.clear()


    def last_card_dealt(self):
        print(self.name + ' is dealt a ' + self.hand[-1].__str__())


    def dealers_top_card(self):
        print(self.name + ' Top Card: ' + self.hand[-1].__str__())


    def score_hand(self):

        scores = {'Ace': (1, 11),
                  'Two': 2,
                  'Three': 3,
                  'Four': 4,
                  'Five': 5,
                  'Six': 6,
                  'Seven': 7,
                  'Eight': 8,
                  'Nine': 9,
                  **dict.fromkeys(['Ten', 'Jack', 'Queen', 'King'], 10)}

        ace_in_hand = False
        soft_ace = False
        score = 0


        # print('in score_hand, this should be 0 --> ' + str(score))
        for card in self.hand:
            rank = card.get_rank()
            if rank == 'Ace' and ace_in_hand is True:
                score += 1
            elif rank == 'Ace':
                ace_in_hand = True
            else:
                score += scores.get(rank)
                # print('No Ace: score += scores.get(rank) --> ' + str(score))


        if ace_in_hand:
            if score + scores.get('Ace')[1] > 21:
                score += scores.get('Ace')[0]
                # print("Hard Ace: score += scores.get('Ace')[0] --> " + str(score))
            else:
                score += scores.get('Ace')[1]
                # print("Soft Ace: score += scores.get('Ace')[1] --> " + str(score))
                soft_ace = True



        # print('right before "if score > 21....print player busts", score --> ' + str(score))
        if score > 21:
            print(self.name + " busts with " + str(score))
            self.score = 1


        elif 1 < score < 22:
            # print('in "elif 1 < score < 22" w/ print after, score --> ' + str(score))
            if soft_ace:
                print(self.name + "'s score: Soft " + str(score))
            if not soft_ace:
                print(self.name + "'s score: " + str(score))

            self.score = score
        print('\n')


    def show_hand(self):
        print(self.name + "'s hand: " + ', '.join([card.__str__() for card in self.hand]))
        self.score_hand()


    def play_dealer_hand(self, shoe):
        self.show_hand()
        while self.score < 17:
            print('The Dealer Hits.')
            self.add_card_to_hand(shoe.deal_card())
            self.last_card_dealt()
            self.score_hand()
            if self.score == 1:
                break
        if 17 <= self.score <= 21:
            print(self.name + ' stays with ' + str(self.score))

    def check_for_blackjack(self):

        if self.name == 'The Dealer':
            print('Checking for Blackjack...')
            for x in range(3):
                time.sleep(.2)
                print('.')
                time.sleep(.2)
                print('..')
                time.sleep(.2)
                print('...')
                time.sleep(.2)
                print('..')
            time.sleep(.2)
            print('.')

        has_ace = False
        has_ten_point_card = False

        for card in self.hand:
            if card.get_rank() in ['Ten', 'Jack', 'Queen', 'King']:
                has_ten_point_card = True
            if card.get_rank() == "Ace":
                has_ace = True

        return has_ace & has_ten_point_card




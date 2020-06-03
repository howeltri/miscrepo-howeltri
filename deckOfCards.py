import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f'{self.value} of {self.suit}'

class Deck:

    def __init__(self):
        self.cards = []
        self._gen_cards()
        self.cur_pos = 0

    def _gen_cards(self):
        pos_values = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.cards = [Card(suit, value) for value in pos_values for suit in suits]

    def count(self):
        return len(self.cards)

    def _display_deck(self):
        for card in self.cards:
            print(card)

    def shuffle(self):
        shuffled = []
        if self.count() != 56:
            raise ValueError('Only full decks can be shuffled')
        for i in range(55,-1,-1):
            shuffled.append(self.cards.pop(random.randint(0, i)))
        self.cards = shuffled

    def _deal(self, num):
        removed = []
        if self.count() == 0:
            raise ValueError('Deck empty!')
        while num>0 and self.count() != 0:
            removed.append(self.cards.pop(num))
            num -= 1
        return removed

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)

    def __repr__(self):
        return f'Deck of {self.count()} cards'

    def __iter__(self):
        return iter(self.cards)

    def __next__(self):
        try:
            self.cur_pos +=1
            print('IIII')
            return self.cards[self.cur_pos]
        except StopIteration("End of Deck!"):
            pass

def main():

    deck1 = Deck()
    # deck1._display_deck()
    # deck1.shuffle()
    # deck1._display_deck()
    # deck1._deal(10)
    # print(deck1)
    # print(deck1.deal_hand(10))
    for i in deck1:
        print(i)


if __name__ == '__main__':
    main()








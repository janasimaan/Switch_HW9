import random
from card import Card


class Board:
    def __init__(self, size):
        self.size = size
        self.cards = self._create_shuffled_cards()

    def _create_shuffled_cards(self):
        cards = [Card(i) for i in range(self.size // 2) for _ in range(2)]
        random.shuffle(cards)
        return cards

    def _display_board(self):
        for i, card in enumerate(self.cards):
            print(f"{card.value:2}" if card.face_up else " *", end=" ")
            if (i + 1) % (self.size // 2) == 0:
                print()
        print()

    def flip_card(self, index):
        self.cards[index].flip()

    def _is_valid_index(self, index):
        return 0 <= index < len(self.cards)

    def _is_match(self, index1, index2):
        return self.cards[index1].value == self.cards[index2].value





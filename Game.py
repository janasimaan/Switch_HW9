class game:
    def __init__(self, board):
        self.board = board

    def play(self):
        pairs_found = 0
        turns = 0

        while pairs_found < self.board.size // 2:
            self.board._display_board()
            index1, index2 = self._get_valid_indices()

            self.board.flip_card(index1)
            self.board.flip_card(index2)
            self.board._display_board()

            if self.board._is_match(index1, index2):
                print("Match found!")
                pairs_found += 1
            else:
                print("No match. Try again.")
                self.board.flip_card(index1)
                self.board.flip_card(index2)

            turns += 1

        print(f"Congratulations! You completed the game in {turns} turns.")

    def _get_valid_indices(self):
        while True:
            try:
                index1 = int(input("Enter the index of the first card: "))
                index2 = int(input("Enter the index of the second card: "))
                if index1 != index2 and self.board._is_valid_index(index1) and self.board._is_valid_index(index2):
                    return index1, index2
                print("Invalid indices. Please choose two different valid indices.")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")